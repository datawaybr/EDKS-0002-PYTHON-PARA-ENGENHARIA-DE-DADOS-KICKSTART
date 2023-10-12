# Variáveis

# string
name = "Bob"
# int
age = 23


# str.format()
string = "Hello, {}. You are {}.".format(name, age)

# f-strings
string = f"Hello, {name}. You are {age}."

long_string = f"""
    SELECT *
      FROM users
     WHERE name = '{name}'
"""

print(long_string)

# upper
upper = long_string.upper()
print(upper)

#lower
lower = long_string.lower()
print(lower)

#split
sentence = "frase de exemplo"
words = sentence.split()  # separar por espaços em branco
print(words)

sentence2 = "exemplo-de-tag"
words2 = sentence2.split("-")  # separar por espaços em branco
print(words2)

# Primeiro item da lista
print(words[0])

# Ultimo item da lista
print(words[2])

# Ultimo item da lista dinamicamente
length = len(words)
print(f"tamanho da lista: {length}")

#print(words[length])
print(words[length - 1])


#join 
string_list = ["Esta", "é", "uma", "lista", "de", "strings"]
complete_sentence = " ".join(string_list)  # Join with spaces
print(complete_sentence)

#starts or endswith
text = "Hello, World!"

starts_with_hello = text.startswith("Hello")
print(f"inicia com hello: {starts_with_hello}")

ends_with_world = text.endswith("World")
print(f"termina com world: {ends_with_world}")

# contains
text = "Hello, World!"
contains_hello = "Hello" in text
print(f"contem hello: {contains_hello}")