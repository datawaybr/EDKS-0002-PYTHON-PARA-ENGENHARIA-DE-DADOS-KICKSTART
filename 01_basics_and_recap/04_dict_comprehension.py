data = {
    'class': 'Formula 1',
    'name': 'Lewis Hamilton',
    'nationality': 'British',
    'team': 'Mercedes'
}

# Novo dicionário com for loop
new_data_for_loop = {}

for chave, valor in data.items():
    new_data_for_loop[chave] = valor.upper()

print(new_data_for_loop)


# Novo dicionário com Dict Comprehension
new_data_dict_comp = {chave: valor.upper() for chave, valor in data.items()}
print(new_data_dict_comp)


# Novo dicionário com Dict Comprehension e if
new_data_dict_comp = {chave: valor.upper() for chave, valor in data.items() if chave in ['team', 'name']}
print(new_data_dict_comp)