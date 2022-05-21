import nltk
from nltk import word_tokenize

from urllib import request, response

url = "https://kmartinez24.github.io/Temporal2/PLN.txt"
#Dando click a raw seria asi:
# url = "https://raw.githubusercontent.com/Kmartinez24/Temporal2/gh-pages/PLN.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")
