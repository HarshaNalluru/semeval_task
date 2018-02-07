from xml.dom import minidom
from xml.etree import ElementTree
import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Harsha is looking at buying golden apple for $1 billion')

# for token in doc:
#     print(token.text,"\t:" ,token.lemma_, token.pos_, token.tag_, token.dep_,
#           token.shape_, token.is_alpha, token.is_stop)


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)



root = ElementTree.parse('dev-data.xml').getroot()
print(root.getchildren()[0].getchildren()[0].text)
print(root.getchildren()[0].getchildren()[1].getchildren()[0].attrib['text'])


doc = nlp(root.getchildren()[0].getchildren()[0].text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
