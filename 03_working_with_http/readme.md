# Requisições HTTP

[GoRest](https://gorest.co.in/) REST API online e gratuita para testes e prototipagem.

## Principais códigos de resposta HTTP

200: OK. Tudo funcionou como esperado.
201: Um recurso foi criado com sucesso em resposta a uma solicitação POST. O cabeçalho Location contém o URL apontando para o novo recurso criado.
204: A solicitação foi tratada com sucesso e a resposta não contém conteúdo do corpo (como uma solicitação DELETE).

400: Bad request. Isso pode ser causado por várias ações do usuário, como fornecer dados JSON inválidos no corpo da solicitação etc.
401: Unauthorized. O usuário não está autenticado. Isso geralmente acontece quando o usuário não fornece credenciais válidas no cabeçalho da solicitação.
404: Not found. O recurso solicitado não existe.

500: Internal server error. Isso significa que ocorreu um erro no servidor. Geralmente é um erro no código do servidor.

