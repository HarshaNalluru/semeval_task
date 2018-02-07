from xml.dom import minidom
from xml.etree import ElementTree

root = ElementTree.parse('dev-data.xml').getroot()

print(root.getchildren()[0].getchildren()[0].text)
print(root.getchildren()[0].getchildren()[1].getchildren()[0].attrib['text'])