'''
Programa realizado por:
    Héctor Eduardo Camberos Ochoa
    ICI 6°B
'''

import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

url = "https://hcamberos.github.io/CELN/"

html = request.urlopen(url)

htmlParse = BeautifulSoup(html, 'html.parser')

text = htmlParse.get_text()
tokens = word_tokenize(text)
title = htmlParse.title

print(f"Titulo: {title}")

print(f"Tipo: {type(tokens)}")

print(f"El total de tokens es: {len(tokens)}")
print(tokens[:15])
