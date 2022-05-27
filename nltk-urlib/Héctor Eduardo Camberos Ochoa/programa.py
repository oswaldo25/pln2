'''
Programa realizado por:
    Héctor Eduardo Camberos Ochoa
    ICI 6°B
'''

import nltk
from nltk import word_tokenize
from urllib import request, response

url = "https://hcamberos.github.io/CELN/"

response = request.urlopen(url)
rawAlejandro = response.read().decode('utf8')

tokens = word_tokenize(rawAlejandro)

print("Tokens es: ",type(tokens),"\n")
print("Cantidad de tokens: ",len(tokens),"\n")
print("Primeros 15 tokens: ",tokens[:15],"\n")

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")
