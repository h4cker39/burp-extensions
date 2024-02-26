# burp-extensions


Projeto feito com Jython para usar-la precisa baixar o projeto do site official: https://www.jython.org/
  
  Tambem foi usado a lib requests então seria importante importar-la
  java -jar jython-standalone-2.7.2.jar -m ensurepip
  java -jar jython-standalone-2.7.2.jar -m ensure pip upgrade --pip
  java -jar jython-standalone-2.7.2.jar -m ensure pip install requests
  
  

ConvertGet.py Converte reqs de POST com parametros para GET com parametros e envia req, caso responda com 200 ele informa caso contrário informa que não houve sucesso:
#REQUISICAO COM POST 

<img width="1311" alt="Captura de Tela 2024-02-26 às 17 37 28" src="https://github.com/h4cker39/burp-extensions/assets/14226200/1cf6463e-e02e-46fd-8242-8ff440adac5d">


#RESPOSTA JA TRANSFORMADO COM STATUS 200 CASO SEJA VULNERAVEL
<img width="1322" alt="Captura de Tela 2024-02-26 às 17 37 04" src="https://github.com/h4cker39/burp-extensions/assets/14226200/ac8c61bb-f34c-4b82-845d-ea1236ccc919">




#CHECK FOR PII

CheckCpf.py projeto que checa por PII mais especifico para CPF, sendo assim ele retorna caso encontre algum dado de CPF e valida se o cpf é verdadeiro.


<img width="1311" alt="Captura de Tela 2024-02-26 às 17 31 07" src="https://github.com/h4cker39/burp-extensions/assets/14226200/2b636345-4a27-4654-9516-ed1560a11796">



  

