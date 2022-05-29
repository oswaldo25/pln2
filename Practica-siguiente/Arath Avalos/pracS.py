import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize


url = "https://www.iic.uam.es/inteligencia/que-es-procesamiento-del-lenguaje-natural/#:~:text=El%20Procesamiento%20del%20Lenguaje%20Natural,el%20ingl%C3%A9s%20o%20el%20chino."

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