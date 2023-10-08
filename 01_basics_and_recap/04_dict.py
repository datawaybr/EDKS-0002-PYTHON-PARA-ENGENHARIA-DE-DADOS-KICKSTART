# Dictionaries

# Chave: Valor
print("-------- IMPRIMIR TODOS ELEMENTOS ----------")

data = {
    'class': 'Formula 1',
    'name': 'Lewis Hamilton',
    'nationality': 'British',
    'team': 'Mercedes'
}
print(data)

print("-------- ACESSAR UM ELEMENTO ----------")

# Acessando elementos de um dicionário
nome = data['name']
nome2 = data.get('name', 'sem nome')
print(f"driver: {nome}")
print(f"driver: {nome2}")

print("-------- ADICIONAR UM ELEMENTO ----------")

#Adicionando elementos a um dicionário
data['age'] = 38
print(data)

print("-------- REMOVER UM ELEMENTO ----------")

# Removendo elementos de um dicionário
del data['age']
print(data)

print("-------- ALTERAR UM ELEMENTO ----------")

# Alterar elementos de um dicionário
data['team'] = 'McLaren'
print(data)


print("-------- LOOP EM UM DICIONÁRIO ----------")
# Como fazer loop em um dicionário

print("-------- data ----------")
for item in data:
    print(f"{item}")

print("-------- data.keys() ----------")
for item in data.keys():
    print(f"{item}")

print("-------- data.values() ----------")
for item in data.values():
    print(f"{item}")

print("-------- data.items() ----------")
for chave, valor in data.items():
    print(f"{chave} : {valor}")
