'''Jazmin Azucena Gonzalez Peredia / Programa 9 / Parcial 2'''
import nltk
from urllib import request
from bs4 import BeautifulSoup
from nltk.probability import FreqDist

url = "https://www.viewnext.com/que-es-pln-procesamiento-lenguaje-natural/"
response = request.urlopen(url)
contenidoPagina = BeautifulSoup(response, 'html.parser')

text = contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)

print(f"Total tokens: {len(tokens)}")
print(tokens[:5])

text_tokens = nltk.Text(tokens)
text.findall("<lenguaje>(<.*>)")
text.concordance("lenguaje")

#HTML word
htmlwords = htmlwords = ['https', 'http', 'display', 'button', 'hover',
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

# Create NLTK Text instance to use NLTK APIs
text2 = nltk.Text(words)
# Create Frequency distribution to see frequency of words
freqdist = FreqDist(text2)
freqdist.plot(20)
freqdist.plot(20, cumulative=True)