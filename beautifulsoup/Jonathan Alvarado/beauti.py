import nltk
from urllib import request
from bs4 import BeautifulSoup

url = "https://jonyav.github.io/fime/pagina.html"
response = request.urlopen(url)
contenidoPagina = BeautifulSoup(response,'html.parser')

text = contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)
title = contenidoPagina.title
print(f"Print the title: {title}")
print(text)
print(f"type: {type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

text_tokens = nltk.Text(tokens)
text_tokens.findall("<PLN>(<.*>)")
text_tokens.concordance("PLN")