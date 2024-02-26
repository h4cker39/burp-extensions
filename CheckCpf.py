from burp import IBurpExtender
from burp import IHttpListener
import re
from validacpf import CheckCpf
class BurpExtender(IBurpExtender, IHttpListener):
  def registerExtenderCallbacks(self, callbacks):
    self.callbacks = callbacks
    self.helpers = callbacks.getHelpers()
    callbacks.setExtensionName("Detecta CPF/PII em respostas")
    callbacks.registerHttpListener(self)

  def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
    resposta = messageInfo.getResponse()
    objValidaCpf = CheckCpf()
    objValidaCpf.main(resposta)
    if resposta:
        resposta = self.helpers.bytesToString(resposta)
        pattern = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
        pattern2 = r'\b\d{11}\b'
        #muita das vezes não existe formatacao no cpf então pegar 11 numeros sequenciais 
        #pode ser uma tatica para identificar principalmente se vier por api
        #é importante lembrar que não é necessário da req pois seria na resposta aonde estamos
        #buscando
        padrao = re.findall(pattern, resposta)
        padrao2 = re.findall(pattern2, resposta)
        if padrao:
            for i in padrao:
                #objValidaCpf.main(i)
                self.callbacks.printOutput(self.helpers.bytesToString(messageInfo.getRequest()))
        else:
            print("Error: No response available.")

       
