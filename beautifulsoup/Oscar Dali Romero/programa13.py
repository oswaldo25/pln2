'''
Oscar Dalí Nattaniel Romero Raygoza    6°B    ICI
'''

import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

url = "https://daliromero.github.io/CenlaN/index.html"

html = request.urlopen(url)

htmlParse = BeautifulSoup(html, 'html.parser')

tokens = [] 

for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())

print(type(tokens))
print(len(tokens))
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<computo>(<.*>)")
text.concordance("computo")
