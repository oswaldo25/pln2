import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
from urllib import request
from nltk.probability import FreqDist


url="https://www.ctisoluciones.com/blog/como-funciona-procesamiento-lenguaje-natural-pnl"
response = request.urlopen(url)
readhtml=BeautifulSoup(response,'html.parser')


text=readhtml.get_text()
tokens=nltk.word_tokenize(text)
title=readhtml.title

print(text)
print(f"Print the title: " ,(title))
print(f"type: ", (type(text)))
print(f"Total tokens: ", (len(tokens)))
print(tokens[:15])
tokens = []

for parsers in readhtml.find_all("p"):
    tokens=tokens + word_tokenize(parsers.get_text())

print(type(tokens))
print("Total de palabras: ",len(tokens))
print(tokens)

text=nltk.Text(tokens)
text.findall("<chatbots>(<.*>)")
text.concordance("chatbots")



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


words = [w for w in tokens if w.isalpha() and len(w) > 4 and w.lower() not in htmlwords]
# Create NLTK Text instance to use NLTK APIs\par
text2 = nltk.Text(words)
# Create Frequency distribution to see frequency of words\par
freqdist = FreqDist(text2)
freqdist.plot(15)
freqdist.plot(15, cumulative=True)