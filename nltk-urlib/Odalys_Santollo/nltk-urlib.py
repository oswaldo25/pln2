import nltk
from nltk import word_tokenize

from urllib import request

url = "https://odalys-santollo.github.io/fime/lenguaje.txt"
response = request.urlopen(url)
row = response.read().decode('utf8')

tokens = word_tokenize(row)
print(type(tokens))
print(len(tokens))
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<lenguas>(<.*>)")
text.concordance("lenguas")