import xml.etree.ElementTree as ET

vehicle_xml_data_as_string = "<motorvehicles><vehicle type='car'><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle type='van'><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle></motorvehicles>"

root = ET.fromstring(vehicle_xml_data_as_string)

print("Root Tag:")
print(root.tag)

print("\nRoot Attributes:")
print(root.attrib)

print("\nIterate the children nodes:")

for child in root:
    print(child.tag, child.attrib)

print("\nAccessing by index:")
root[0][1].text

print("\nAccessing atttributes:")
for attr in root[0].attrib:
    print(attr + "=" + root[0].attrib[attr])

print("\nSearching with Iter:")
for element in root.iter(tag='registration_no'):
    print(element.text)

print("\nSearching with findall:")
for element in root.findall('vehicle'):
    regno = element.find('registration_no').text
    make = element.find('make').text
    print(regno, make)

print("\nModifying XML:")
for element in root.iter(tag='make'):
    newmake = 'Nissan'
    element.text = newmake

print("\nSearching after modifying:")
for element in root.findall('vehicle'):
    regno = element.find('registration_no').text
    make = element.find('make').text
    print(regno, make)

print("Building XML:")
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

# Additional Resources

# Python ElementTree library official documentation: https://docs.python.org/3/library/xml.etree.elementtree.html

# An advanced tutorial on XML processing with Python: https://realpython.com/python-xml-parser/


def test_2():
    vehicle_xml_data_as_string = "<motorvehicles><vehicle><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle><vehicle><registration_no>DE2115</registration_no><make>TATA</make><model>Sumo</model></vehicle><vehicle><registration_no>CAR7785</registration_no><make>Kia</make><model>Optima</model></vehicle></motorvehicles>"

    root = ET.fromstring(vehicle_xml_data_as_string)
    for element in root.findall('vehicle'):
        reg_no = element.find('registration_no').text
        if reg_no == 'DE2115':
            make = element.find('make')
            make.text = 'Nissan'
            model = element.find('model')
            model.text = 'Skyline'

    for element in root.findall('vehicle'):
        make = element.find('make')
        if make.text == 'Nissan':
            reg_no = element.find('registration_no').text
            print(reg_no)


# json reference
# https://docs.python.org/3/library/json.html
# https://realpython.com/python-json/
