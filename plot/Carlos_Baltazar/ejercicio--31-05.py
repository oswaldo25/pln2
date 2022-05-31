import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.probability import FreqDist


url = "https://www.iic.uam.es/inteligencia/que-es-procesamiento-del-lenguaje-natural/"

html = urllib.request.urlopen(url)

htmlParse = BeautifulSoup(html, 'html.parser')

tokens = []
for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())

title = htmlParse.title
print("----------------------------------")
print("Titulo: ")
print(title)
print("----------------------------------")
print(type(tokens))
print(len(tokens))
print(tokens)

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")


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
            'center', 'false', 'right', 'cookies']
#\par
words = [w for w in tokens if w.isalpha() and len(w) > 4 and w.lower() not in htmlwords]
# Create NLTK Text instance to use NLTK APIs\par
text2 = nltk.Text(words)
# Create Frequency distribution to see frequency of words\par
freqdist = FreqDist(text2)
freqdist.plot(20)
freqdist.plot(20, cumulative=True)