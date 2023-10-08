from pprint import pprint
import xml.etree.ElementTree as ET
import dicttoxml

# Read XML
tree = ET.parse('file_1.xml')
root = tree.getroot()

# Find all "item" in xml
for elem in root:
    for subelem in elem.findall('item'):
        # if we don't need to know the name of the attribute(s), get the dict
        
        # Attributes
        pprint(type(subelem.attrib))
        pprint(subelem.attrib)
        
        # Text
        pprint(subelem.text)

        # if we know the name of the attribute, access it directly
        pprint(subelem.get('name'))
        pprint("-----")

# Save XML
data = {
    'name': 'Lewis Hamilton',
    'nationality': 'British',
    'team': 'Mercedes'
}

xml = dicttoxml.dicttoxml(data)

with open("file2.xml", "w") as f:
    f.write(str(xml,"utf-8"))