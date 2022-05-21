'''Programa github web'''
'''Axel Hervey Cruz Baez'''
'''Oswaldo Carrillo Zepeda'''

import nltk
from nltk import word_tokenize

from urllib import request, response

url="https://cow01.github.io/NLPWEB/Arfinal.txt"
response = request.urlopen(url)
raw=response.read().decode('utf8')

tokens = word_tokenize(raw)
print(f"\n{type(tokens)}")
print(f"\nCantidad texto: {len(tokens)}")
print(f"\n{tokens[:15]}")

text=nltk.Text(tokens)
print("\n")
text.findall("<algoritmo><.*>")
print("\n")
text.concordance("algoritmo")
