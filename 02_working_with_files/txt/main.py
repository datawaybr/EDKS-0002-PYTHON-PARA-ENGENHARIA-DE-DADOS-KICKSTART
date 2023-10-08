from pprint import pprint

# Single line
with open('file_1.txt', 'r') as file:
    contents = file.read()
    pprint(contents)

# Multiple lines
# Explain \n
with open('file_2.txt', 'r') as file:
    contents = file.read().splitlines()
    pprint("-----")

    for line in contents:
        pprint(line)

# Write
with open('file_3.txt', 'w') as file:
    file.write('Hello\nWorld!')