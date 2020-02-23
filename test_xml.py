import xml.etree.cElementTree as ET

greetings = ET.Element("greetings")

name = ET.SubElement(greetings, "name")
name.text = 'Wojtek'
msg = ET.SubElement(greetings, "msg")
msg.text = 'Hello World'

s = ET.tostring(greetings)
print(s)
