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
        if padrao or padrao2:
            for i in padrao:
                #check_cpf(i)
                self.callbacks.printOutput(self.helpers.bytesToString(messageInfo.getRequest()))
        else:
            print("Error: No response available.")
    cpf_completo = [0] * 11
  
  def valida10(cpf_completo, restante):
            novo_cpf = cpf_completo
            print("NOVO CPF AQUI")
            print(novo_cpf)
            main = [0]*9
            sacret_digit = cpf_completo[0] # pegando o ultimo digito
            cpf_completo.pop(0)
             
            novos_digitos = [10,9,8,7,6,5,4,3,2]
            print( novo_cpf)
            for i in range(9):
                main[i] = int(novos_digitos[i]) * int(cpf_completo[i])
            remainder = sum(main)%11
            if(remainder == 0 or remainder == 1):
                novo_cpf.insert(10,0)
            new_digit = 11-remainder
            novo_cpf.insert(0,sacret_digit)
            novo_cpf.insert(10, new_digit)
            print("Agora sim")
            print(novo_cpf)
            array = [str(item) for item in novo_cpf]
            resultado = ''.join(array)
            print(resultado)
            return resultado
  def valida9(soma, cpf):
        cpf_complete = [char for char in cpf]
        restante = soma % 11

        if restante == 0 or restante == 1:
            cpf_complete.append(0)
        else:
            cpf_complete.append(11 - restante)

        return CheckCpf.valida10(cpf_complete, restante)

  def validarCpf(cpf):
        digitos_convertidos = []
        for char in cpf:
            if char.isdigit():
                digitos_convertidos.append(int(char))
        
        main = [0] * 9
        novos_digitos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        primeiros_nove = digitos_convertidos[:9]
        for i in range(9):
            main[i] = novos_digitos[i] * primeiros_nove[i]
        return CheckCpf.valida9(sum(main), cpf)

  def check_cpf(cpf):
            new_cpf = cpf[:-2]
            vart = validarCpf(str(new_cpf))
            if vart == cpf:
                 print("PII confirmado")
