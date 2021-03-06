#Gabriel Portillo Gonzalez

import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize

url = "https://www.sas.com/es_ar/insights/analytics/what-is-natural-language-processing-nlp.html"

html = urllib.request.urlopen(url)

htmlParse = BeautifulSoup(html, 'html.parser')

text = htmlParse.get_text()
tokens = word_tokenize(text)
title = htmlParse.title

print(f"Titulo: {title}")

tokens = []
for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())


print(type(tokens))
print(len(tokens))
print(tokens)

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")
