numbers = [1, 2, 3, 4, 5]


for_squared_numbers = []

for num in numbers:
    for_squared_numbers.append(num ** 2)

print(f"resultado com for: {for_squared_numbers}")


## List Comprehension

numbers = [1, 2, 3, 4, 5]

# for num in numbers
#     num ** 2
comprehension_squared_numbers = [ num ** 2 for num in numbers ]
print(f"resultado com comprehension: {comprehension_squared_numbers}")
