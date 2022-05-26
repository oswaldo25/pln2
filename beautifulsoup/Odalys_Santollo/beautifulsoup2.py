'''Santollo Vargas Odalys Sarahi/ Programa 7 / Parcial 2'''
import nltk
from urllib import request
from bs4 import BeautifulSoup


url = "https://www.viewnext.com/que-es-pln-procesamiento-lenguaje-natural/"
response = request.urlopen(url)
contenidoPagina = BeautifulSoup(response, 'html.parser')

text = contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)
title = contenidoPagina.title
print(f"print the title : {title} ")
print(text)
print(f"type: {type(tokens)}")
print(f"total tokens: {len(tokens)}")
print(tokens[:15])

text_tokens = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")