# -*- coding: utf-8 -*-
import requests
from burp import IBurpExtender
from burp import ITab
from burp import IProxyListener
from java.awt import Panel
from java.io import PrintWriter
from threading import Thread
from burp import IHttpRequestResponse
from burp import IHttpListener
from burp import IHttpService
from urllib import urlencode
from burp import IParameter
from burp import IRequestInfo
import requests
#By Luis Giordano @Fr0$ty
#Foi me pedido com urgencia então visualmente não inclui mais nada.
#Pega requisicao do Burp que for POST pega os parametros no método processHttpMessage() e envia no GET com a lib import requests


class BurpExtender(IBurpExtender, IProxyListener, IHttpListener):

    def makeGetWithParams(self, url_burp, parameters):
        params = urlencode([(self.helpers.bytesToString(p.getName()), self.helpers.bytesToString(p.getValue())) for p in parameters if p.getType() == IParameter.PARAM_BODY])
        final_url = url_burp.toString() + "?" + params
        r = requests.get(final_url)
        if r.status_code == 200:
                print("GET executed successfully: " + str(final_url))
        else:
                print("URL is not vulnerable to use GET: " + str(final_url))
        return r

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Convert POST parameters to GET")
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):  
            requester = self.helpers.analyzeRequest(messageInfo)
            only_header = "application/x-www-form-urlencoded"
            dec = only_header in self.helpers.bytesToString(messageInfo.getRequest())
            if requester.getMethod() == "POST" and dec:                                                                          
                analyzed_request = self.helpers.analyzeRequest(messageInfo)
                url_burp = analyzed_request.getUrl()
                parameters = self.helpers.analyzeRequest(messageInfo.getRequest()).getParameters()
                r = self.makeGetWithParams(url_burp, parameters)

        

        
