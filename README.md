# burp-extensions


Projeto feito com Jython para usar-la precisa baixar o projeto do site official: https://www.jython.org/
  
  Tambem foi usado a lib requests então seria importante importar-la
  ```
  java -jar jython-standalone-2.7.2.jar -m ensurepip
  java -jar jython-standalone-2.7.2.jar -m ensure pip upgrade --pip
  java -jar jython-standalone-2.7.2.jar -m ensure pip install requests
  ```

  

ConvertGet.py Converte reqs de POST com parametros para GET com parametros e envia req, caso responda com 200 ele informa caso contrário informa que não houve sucesso:
#REQUISICAO COM POST 
[UPDATES] Itens de sec, melhorias de performance, qualidade e boas práticas adcionados, havia um bug no projeto que fazia a query de forma errada, então isto foi ajustado tambem.

 ![Captura de Tela 2024-03-07 às 17 54 58](https://github.com/h4cker39/burp-extensions/assets/14226200/3973b190-fe12-446b-a532-f05771066880)



#RESPOSTA JA TRANSFORMADO COM STATUS 200 CASO SEJA VULNERAVEL

![Captura de Tela 2024-03-11 às 15 29 59](https://github.com/h4cker39/burp-extensions/assets/14226200/63ad1d46-f61e-4020-9851-531d3a2190b8)



#CHECK FOR CPF

CheckCpf.py projeto que checa por PII mais especifico para CPF, sendo assim ele retorna caso encontre algum dado de CPF e valida se o cpf é verdadeiro.
[UPDATES] Itens de sec, melhorias de performance, qualidade e boas práticas adcionados, um bug inerente a detection de cpf também foi validado.

![Captura de Tela 2024-03-11 às 16 03 15](https://github.com/h4cker39/burp-extensions/assets/14226200/40338046-69e9-459c-8bb4-d6b5f82790bf)

  

