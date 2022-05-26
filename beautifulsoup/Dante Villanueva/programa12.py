from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize
from urllib import request

url = "https://dantevl20.github.io/PLN/"
response = request.urlopen(url)
contenidoPagina = BeautifulSoup(response, 'html.parser')

text = contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)
title = contenidoPagina.title
print(f"Print the title: {title}")
print(text)
print(f"type: {type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

text_tokens = nltk.text(tokens)
text_tokens.findall("<PLN>(<.*)")
text_tokens.concordance("PLN")
