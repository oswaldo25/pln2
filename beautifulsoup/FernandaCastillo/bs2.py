'''Fernanda Castillo'''

import nltk
from bs4 import BeautifulSoup
from urllib import request


url="https://decidesoluciones.es/procesamiento-del-lenguaje-natural-pln-o-nlp-que-es-y-para-que-se-utiliza/"
response = request.urlopen(url)

contenidoPagina=BeautifulSoup(response,'html.parser')

text=contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)
title=contenidoPagina.title

print(f"Print the title:{title}")
print(text)
print(f"type:{type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

text_tokens=nltk.Text(tokens)
text_tokens.findall("<PLN>(<.*>)")
text_tokens.concordance("PLN")