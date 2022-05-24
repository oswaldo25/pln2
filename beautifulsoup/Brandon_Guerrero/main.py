import nltk
import urllib.request
from nltk import word_tokenize
from bs4 import BeautifulSoup

url = "https://www.iberdrola.com/innovacion/procesamiento-lenguaje-natural-pln"
html = urllib.request.urlopen(url)
htmlParse = BeautifulSoup(html, 'html.parser')

tokens = []
for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())
print(f"\n{type(tokens)}")
print(f"\n{len(tokens)}")
print(f"\n{tokens}")

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
print("\n")
text.concordance("PLN")