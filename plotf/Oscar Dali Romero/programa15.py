'''
Oscar Dalí Nattaniel Romero Raygoza    6°B    ICI
'''

import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.probability import FreqDist

url = "https://daliromero.github.io/PLN/componentes_pln"

html = request.urlopen(url)

htmlParse = BeautifulSoup(html, 'html.parser')

text = htmlParse.get_text()
tokens = word_tokenize(text)
title = htmlParse.title

print(f"Titulo: {title}")

print("-----------------------------------------------------")

print(f"type: {type(tokens)}")

print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

print("-----------------------------------------------------")

text = nltk.Text(tokens)
text.findall("<lenguaje>(<.*>)")
text.concordance("lenguaje")

print("-----------------------------------------------------")

htmlwords = ['https', 'http', 'display', 'button', 'hover', 'color', 'background', 'height', 'none', 
'target', 'WebPage', 'reload', 'fieldset', 'padding', 'input', 'select', 'textarea', 'html', 'form', 
'cursor', 'overflow', 'format', 'italic', 'normal', 'truetype', 'before', 'name', 'label', 'float', 
'title', 'arial', 'type', 'block', 'audio', 'inline', 'canvas', 'margin', 'serif', 'menu', 'woff', 
'content', 'fixed', 'media', 'position', 'relative', 'hidden', 'width', 'clear', 'body', 'standard', 
'expandable', 'helvetica', 'fullwidth', 'embed', 'expandfull', 'fullstandardwidth', 'left', 'middle', 
'iframe', 'rgba', 'selected', 'scroll', 'opacity', 'center', 'false', 'right']

words = [w for w in tokens if w.isalpha() and len(w) > 4 and w.lower() not in htmlwords]

text2 = nltk.Text(words)

freqdist = FreqDist(text2)
freqdist.plot(20)
freqdist.plot(20, cumulative=True)