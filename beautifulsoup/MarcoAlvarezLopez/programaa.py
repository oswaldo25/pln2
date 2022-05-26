import nltk
from nltk import word_tokenize
# importing modules
import urllib.request
from bs4 import BeautifulSoup

# providing url
url = "https://decidesoluciones.es/procesamiento-del-lenguaje-natural-pln-o-nlp-que-es-y-para-que-se-utiliza/"

# opening the url for reading
html = urllib.request.urlopen(url)

# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')

tokens = []
# getting all the paragraphs
for para in htmlParse.find_all("p"):
    tokens = tokens + word_tokenize(para.get_text())


print(len(tokens))
print(tokens)

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")