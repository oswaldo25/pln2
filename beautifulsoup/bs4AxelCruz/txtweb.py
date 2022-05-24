'''Axel Hervey Cruz Baez'''

import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
from urllib import request


url="https://decidesoluciones.es/procesamiento-del-lenguaje-natural-pln-o-nlp-que-es-y-para-que-se-utiliza/"
response = request.urlopen(url)

readhtml=BeautifulSoup(response,'html.parser')

tokens = []

for parsers in readhtml.find_all("p"):
    tokens=tokens + word_tokenize(parsers.get_text())

print(type(tokens))
print("Total de palabras: ",len(tokens))
print(tokens)

text=nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")