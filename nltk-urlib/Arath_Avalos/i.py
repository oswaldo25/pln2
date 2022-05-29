import nltk
from nltk import word_tokenize

from urllib import request, response

url = "https://arathnoir.github.io/plnprueba1/nltk.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")