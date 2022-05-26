from lib2to3.pgen2 import token
from httpx import request
from matplotlib.pyplot import title
import nltk
import urllib.request
from nltk import word_tokenize
from bs4 import BeautifulSoup

url = "https://www.iberdrola.com/innovacion/procesamiento-lenguaje-natural-pln"
html = urllib.request.urlopen(url)
htmlParse = BeautifulSoup(html, 'html.parser')

text = htmlParse.get_text()
tokens = nltk.word_tokenize(text)
title = htmlParse.title
print(f"Print the title: {title}")
print(text)
print(f"type: {type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print("\n")
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<procesamiento>(<.*>)")
print("\n")
text.concordance("procesamiento")
