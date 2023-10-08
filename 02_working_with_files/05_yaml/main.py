from pprint import pprint
import yaml


# Load YAML
with open('file_1.yaml') as f:
    try:
        data = yaml.load(f, Loader=yaml.FullLoader)
        pprint(data)
    except Exception as e:
        pprint(e)


# Write YAML
data = {
    'list': [1, 42, 3.141, 1337, 'help'],
    'string': 'bla',
    'dict': {
        'foo': 'bar',
        'key': 'value',
        'bar': 50
    }
}

with open("file_3.yaml", "w") as f:
    yaml.dump(data, f)