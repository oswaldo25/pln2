import nltk
from nltk import word_tokenize
# importing modules
import urllib.request
from bs4 import BeautifulSoup
url = "https://decidesoluciones.es/procesamiento-del-lenguaje-natural-pln-o-nlp-que-es-y-para-que-se-utiliza/"
html = urllib.request.urlopen(url)
htmlParse = BeautifulSoup(html, 'html.parser')
tokens = []
for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())
print(type(tokens))
print(len(tokens))
print(tokens)
text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")