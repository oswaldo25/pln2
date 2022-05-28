import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Ford_GT40"

html = request.urlopen(url)

htmlParse = BeautifulSoup(html, 'html.parser')

text = htmlParse.get_text()
tokens = word_tokenize(text)
title = htmlParse.title

print(f"Titulo: {title}")

#print(text)

print(f"type: {type(tokens)}")

print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

tokens = [] 
for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())
print(type(tokens))
print(len(tokens))
print(tokens[:15])
text = nltk.Text(tokens)
text.findall("<ford>(<.*>)")
text.concordance("ford")