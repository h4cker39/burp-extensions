# -*- coding: utf-8 -*-
from burp import IBurpExtender
from burp import IHttpListener
import re

#Verifica se nas chamadas mais espeicificamente possui dados PII no caso abaixo o CPF.
class BurpExtender(IBurpExtender, IHttpListener):
  def registerExtenderCallbacks(self, callbacks):
    self.callbacks = callbacks
    self.helpers = callbacks.getHelpers()
    callbacks.setExtensionName("Detector de dados PII")
    callbacks.registerHttpListener(self)
 
  def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
    resposta = messageInfo.getResponse()
    if resposta:
        resposta = self.helpers.bytesToString(resposta)
        # A regex ja elimina possibilidade de ataque e na funcao de valida cpf remove caracter invalido
        pattern = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
        pattern2 = r'\b\d{11}\b'
        padrao = re.findall(pattern, resposta)
        padrao2 = re.findall(pattern2, resposta)
        if padrao or padrao2:
            for i in padrao:
                if self.validar_cpf(i) is True:
                    self.callbacks.printOutput("CPF encontrados na req abaixo")
                    self.callbacks.printOutput(self.helpers.bytesToString(messageInfo.getResponse()))
            #segunda opcao para a Regex
            for i in padrao2:
                if self.validar_cpf(i) is True:
                     self.callbacks.printOutput("CPF encontrados na req abaixo")
                     self.callbacks.printOutput(self.helpers.bytesToString(messageInfo.getResponse()))
        else:
                self.callbacks.printOutput(self.helpers.bytesToString(""))
#funcao que valida cpf
  @staticmethod
  def validar_cpf(cpf):
    cpf = cpf.replace('-','')
    cpf = cpf.replace('.','')
    cpf = ''.join(filter(unicode.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        d1 = 0
    else:
        d1 = 11 - resto
    if d1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        d2 = 0
    else:
        d2 = 11 - resto
    
    if d2 != int(cpf[10]):
        return False
    return True
