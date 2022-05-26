import nltk
from urllib import request
from bs4 import BeautifulSoup

url = "https://kevinherrera21.github.io/ComputoNube/views/estado.html"
response = request.urlopen(url)
contenidoPagina = BeautifulSoup(response,'html.parser')

text = contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)
title = contenidoPagina.title

print(f"Titulo: {title}")
print(text)
print(f"type: {type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

text_tokens = nltk.Text(tokens)
text_tokens.findall("<nube>(<.*>)")
text_tokens.concordance("nube")