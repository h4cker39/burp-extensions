#Threat Modeling desafio Meli ;)

Threat Modeling possui dois etapas:

O Desenho no qual criado, entry point, exit points, assests, m-processes, processes, data flow e boundaries:

*  	Process 	The process shape represents a task that handles data within the application. The task may process the data or perform an action based on the data.

*   Multiple Process 	The multiple process shape is used to present a collection of subprocesses. The multiple process can be broken down into its subprocesses
 in another DFD.

* Data Store 	The data store shape is used to represent locations where data is stored. Data stores do not modify the data, they only store data.

* Data Flow 	The data flow shape represents data movement within the application. The direction of the data movement is represented by the arrow.

* Privilege Boundary 	The privilege boundary (or trust boundary) shape is used to represent the change of trust levels as the data flows through the application. Boundaries show any location where the level of trust

![Captura de Tela 2024-02-28 às 14 51 05](https://github.com/h4cker39/burp-extensions/assets/14226200/0bccd78e-021f-40a6-b560-b4ca19c29a8a)


 Pontos de atencao:

 Um dos principais pontos encontrados na aba findings da planilha anexo, também fica sob componentes não mapeados, como ausencia de autenticacao, controles de acessos, ausencias de logs e etc conforme nos findings do relatório anexo:
O arquivo do desenho foi executado no draw.io pois uso Linux motivo no qual não fiz no Microsoft Threat Modeling Tool, é eu sei, é triste, não fiz dual boot pois ia gastar meu tempo a mais pra fazer o desafio, coisa que eu não tenho, enfim

![Captura de Tela 2024-02-28 às 14 53 31](https://github.com/h4cker39/burp-extensions/assets/14226200/852d56b7-2307-4b3b-8e75-272a8d39f3b3)


 # Relatório 

 o Relatório possui 3 abas (la em baixo):
 1. Etapa seria as regras negócios conforme descrito
 2. Seria a definicao de STRIDE aonde descreve o que cada letra é associado
 3. Os Findings com os detalhes que foram encontrados pelo desenho



 
