import nltk
from nltk import word_tokenize
import urllib.request
from bs4 import BeautifulSoup

url = "https://jonyav.github.io/fime/pagina.html"
html = urllib.request.urlopen(url)
htmlParse = BeautifulSoup(html, 'html.parser')
tokens = []
for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())

print(type(tokens))
print(len(tokens))
print(tokens[:15])
text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")