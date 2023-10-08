# pip install requests
import requests

response = requests.get("https://gorest.co.in/public/v2/users")


# response.json() retorna um dicionário
print('------ RESPOSTA COMO UMA LISTA DE DICIONÁRIOS ------')
response_json = response.json()
print(f"type: {type(response_json)}")
print(response_json)


# response.text retorna uma string
print('------ RESPOSTA COMO STRING ------')
response_text = response.text
print(f"type: {type(response_text)}")
print(response_text)


# response.status_code retorna o código de status da requisição
print('------ CÓDIGO DE STATUS DA REQUISIÇÃO ------')
response_status_code = response.status_code
print(f"type: {type(response_status_code)}")
print(response_status_code)


# response.headers retorna um dicionário com os cabeçalhos da requisição
print('------ CABEÇALHOS DA REQUISIÇÃO ------')
response_headers = response.headers
print(response_headers)


# Verificando se a requisição foi bem sucedida
print('------ VERIFICANDO SE A REQUISIÇÃO FOI BEM SUCEDIDA ------')
if response.status_code == 200:
    users = response.json()
    
    for user in users:
        print(user)
else:
    print(f"Request falhou com o código: { response.status_code }")