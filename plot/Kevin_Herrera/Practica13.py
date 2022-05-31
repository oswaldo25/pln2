import nltk
from urllib import request
from bs4 import BeautifulSoup
from nltk.probability import FreqDist

url = "https://kevinherrera21.github.io/ComputoNube/views/estado.html"
response = request.urlopen(url)
contenidoPagina = BeautifulSoup(response,'html.parser')

text = contenidoPagina.get_text()
tokens = nltk.word_tokenize(text)
print(text)
print(f"type: {type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

text_tokens = nltk.Text(tokens)
text_tokens.findall("<nube>(<.*>)")
text_tokens.concordance("nube")

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

text2 = nltk.Text(words)

freqdist = FreqDist(text2)
freqdist.plot(20)
freqdist.plot(20, cumulative=True)
