'''Jazmin Azucena Gonzalez Peredia / Programa 8 / Parcial 2'''
from urllib import request
from bs4 import BeautifulSoup
import nltk

url = "https://www.viewnext.com/que-es-pln-procesamiento-lenguaje-natural/"
response = request.urlopen(url)
contenidoPagina = BeautifulSoup(response, 'html.parser')

text = contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)
title = contenidoPagina.title

print(f"Print the title: {title} ")
print(text)
print(f"type: {type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print(tokens[:5])

text_tokens = nltk.Text(tokens)
text.findall("<lenguaje>(<.*>)")
text.concordance("lenguaje")