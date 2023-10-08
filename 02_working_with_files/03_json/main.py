from pprint import pprint
import json

# Read Json
with open('file_1.json', 'r') as file:
    data = json.load(file)
    pprint(f"tipo do dado: {type(data)}")
    pprint('-----')
    pprint(data)

# Save Json
data = {
    'name': 'Lewis Hamilton',
    'nationality': 'British',
    'team': 'Mercedes'
}

with open('file_2.json', 'w') as file:
    json.dump(data, file)