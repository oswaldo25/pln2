from matplotlib.pyplot import text
import nltk
from nltk import word_tokenize
# importing modules
# import urllib.request
from urllib import request
from bs4 import BeautifulSoup
from nltk.probability import FreqDist

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
# Create Frequency distribution to see frequency of words\par
freqdist = FreqDist(text2)
freqdist.plot(20)
freqdist.plot(20, cumulative=True)
