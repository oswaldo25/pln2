from matplotlib.pyplot import text
import nltk
from nltk import word_tokenize
# importing modules
# import urllib.request
from urllib import request
from bs4 import BeautifulSoup

# providing url
url = "https://decidesoluciones.es/procesamiento-del-lenguaje-natural-pln-o-nlp-que-es-y-para-que-se-utiliza/"

# opening the url for reading
response = request.urlopen(url)

# parsing the html file
contenidoPagina = BeautifulSoup(response, 'html.parser')
text = contenidoPagina.get_text()
tokens = word_tokenize(text)
title = contenidoPagina.title

print(title)
print(type(tokens))
print(len(tokens))
print(tokens)

text_tokens = nltk.Text(tokens)
text_tokens.findall("<PLN>(<.*>)")
text_tokens.concordance("PLN")
