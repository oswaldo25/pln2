from lib2to3.pgen2 import token
import nltk
from nltk import word_tokenize

from urllib import request , response

url = "https://jherrera11.github.io/PLN2/zzz.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")