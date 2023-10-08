# Listas
lista1 = []
print('lista1:')
print(lista1)

# Python F-string
texto = f"lista1: {lista1}"
print(texto)

# Lista com elementos
lista2 = [1, 2, 3, 4, 5]
print(f"lista2: {lista2}")

# Lista com elementos de tipos diferentes
lista3 = [1, "dois", 3.0, True, False]
print(f"lista3: {lista3}")

# Adicionando elementos a uma lista
lista3.append(1)
print(f"lista3: {lista3}")

# Permite itens duplicados

# Acessando elementos de uma lista
# print(f"item_1: {lista3[0]}")
print(f"item_1: {lista3[1]}")

# Removendo elementos de uma lista
# primeiro item
lista3.remove(1)
print(f"lista3: {lista3}")

# True
lista3.remove(1)
print(f"lista3: {lista3}")

# ultimo item
lista3.remove(1)
print(f"lista3: {lista3}")

# Alterar elementos de uma lista
lista3[0] = 'um'
print(f"lista3: {lista3}")

# Como fazer loop em uma lista
for item in lista3:
    print(f"item: {item}")

    if type(item) == str:
        print('item é uma string')
    elif type(item) == int:
        print('item é um inteiro')
    elif type(item) == float:
        print('item é um float')
    elif type(item) == bool:
        print('item é um booleano')