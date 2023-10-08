# pip install requests
import requests

url = "https://gorest.co.in/public/v2/users"
token = "a99b738b1b43fdd579eb7a27f86caa6cb479457672377185e3817fa710f41d50"

# POST /users
# Cria um novo usuário

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    "name" : "UserTest",
    "gender":"female",
    "email":"user.teste4@bol.com.br",
    "status":"active"
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 201:
    print("Usuário criado com sucesso!")

    created_user = response.json()
    created_user_id = created_user.get("id")
    print(f"Retorno da requisição POST: ID do usuário criado: {created_user_id}")

    user_endpoint = f"{url}/{created_user_id}"

    user_info = requests.get(user_endpoint, headers=headers)
    print(f"Retorno da requisição GET: {user_info.json()}")

else:
    print("Request falhou com o código:", response.status_code)
    print(response.json())