import csv

# Read csv file (python nativo)
with open('file_1.csv', 'r') as file:
    file = csv.DictReader(file,  delimiter = ',')
    for row in file:
        print(f"type: {type(row)} e valor: {row}")

# Save csv file (python nativo)
data = [
    ['name', 'area', 'country_code2', 'country_code3'],
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
]

with open('file_2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write multiple rows
    writer.writerows(data)