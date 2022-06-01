import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.probability import FreqDist 

url = "https://jherrera11.github.io/PLN2/"

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
text.findall("<NIVEL>(<.*>)")
text.concordance("NIVEL")

htmlwords = ['https', 'http', 'display', 'button', 'hover',
             'color', 'background', 'height', 'none', 'target',
             'WebPage', 'reload', 'fieldset', 'padding', 'input',
            'select', 'textarea', 'html', 'form', 'cursor',
            'overflow', 'format', 'italic', 'normal', 'truetype',
            'before', 'name', 'label', 'float', 'title', 'arial', 'type',
            'block', 'audio', 'inline', 'canvas', 'margin', 'serif', 'menu',
            'woff', 'content', 'fixed', 'media', 'position', 'relative', 'hidden',
            'width', 'clear', 'body', 'standard', 'expandable', 'helvetica',
            'fullwidth', 'embed', 'expandfull', 'fullstandardwidth', 'left', 'middle',
            'iframe', 'rgba', 'selected', 'scroll', 'opacity',
            'center', 'false', 'right']
#\par
words = [w for w in tokens if w.isalpha() and len(w) > 4 and w.lower() not in htmlwords]
# Create NLTK Text instance to use NLTK APIs\par
text2 = nltk.Text(words)
freqdist = FreqDist(text2)
freqdist.plot(20)
freqdist.plot(20, cumulative=True)