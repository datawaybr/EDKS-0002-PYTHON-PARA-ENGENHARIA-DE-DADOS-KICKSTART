# pip install requests
import requests

url = "https://gorest.co.in/public/v2/users"
token = "a99b738b1b43fdd579eb7a27f86caa6cb479457672377185e3817fa710f41d50"
user_id = "5362647"

# POST /users
# Cria um novo usuário

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    "id": user_id
}

user_url = f"{url}/{user_id}"

response = requests.delete(user_url, headers=headers, data=data)

if response.status_code == 204:
    print("Usuário deletado com sucesso!")

else:
    print(f"Request falhou com o código: { response.status_code }")
    print(response.json())
