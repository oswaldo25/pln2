'''Fernanda Castillo'''


import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
from urllib import request
from nltk.probability import FreqDist

#direccion web
url="https://github.com/FerCDD/WEB/blob/main/Componentes.html"
response = request.urlopen(url)
readhtml=BeautifulSoup(response,'html.parser')
text=readhtml.get_text()
tokens=nltk.word_tokenize(text)
title=readhtml.title
#impresion del titulo, el texto de la web, el tipo de dato y la longitud.
print(text)
print(f"Print the title: " ,(title))
print(f"type: ", (type(tokens)))
print(f"Total tokens: ", (len(tokens)))
print(tokens[:15])

text=nltk.Text(tokens)
text.findall("<procesamiento>(<.*>)")
text.concordance("procesamiento")

##Palabras reservadas html
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