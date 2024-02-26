# -*- coding: utf-8 -*-
import requests
from burp import IHttpRequestResponse
from burp import IBurpExtender
from burp import IHttpListener
from burp import IParameter
from burp import IHttpService
from burp import IHttpRequestResponse
#By Luis Giordano @Fr0$ty
#Foi me pedido com urgencia então visualmente não inclui mais nada.
#Pega requisicao do Burp que for POST pega os parametros no método processHttpMessage() e envia no GET com a lib import requests
class BurpExtender(IBurpExtender, IHttpListener):
 
  def registerExtenderCallbacks(self, callbacks):
    self.callbacks = callbacks
    self.helpers = callbacks.getHelpers()
    #callbacks.setExtensionName("Converta requisicao para GET") não testei pois a recrutadora me pediu com urgencia.
    callbacks.registerHttpListener(self)
  def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
    requester =  self.helpers.analyzeRequest(messageInfo)
    if requester.getMethod() == "POST":
      analyzed_request = self.helpers.analyzeRequest(messageInfo)
      url_burp = analyzed_request.getUrl()
      info = ""
      parameters = self.helpers.analyzeRequest(messageInfo.getRequest()).getParameters()
      num_paramters = len(parameters)
      for index, p in enumerate(parameters):
        if(p.getType() == IParameter.PARAM_BODY):
 
          info += self.helpers.bytesToString(p.getName())
          info += '='
          info +=  self.helpers.bytesToString(p.getValue())
          if(index < num_paramters -1):
             info +=  '&'
      url_burp = str(url_burp) + "/"
      final_url = ''.join([str(url_burp), info])    
      r = requests.get(final_url)
 
      if r.status_code == 200 :
          print("GET executado com sucesso : " + str(final_url))
      else:
          print("URL nao esta vulneravel pra usar GET : " + str(final_url))
 
      #hs = callbacks.makeHttpRequest(url)
      #res_status = resposta.getResponse()
      #self.callbacks.printOutput(res_status)
