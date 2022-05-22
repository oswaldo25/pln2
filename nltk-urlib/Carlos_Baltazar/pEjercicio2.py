"""Carlos Alejandro Baltazar Padilla"""

import nltk
from nltk import word_tokenize
from urllib import request, response

url = "https://github.com/Zarlbalt/PLN2/blob/main/act2/texto.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

tokens = word_tokenize(raw)
print(f"\n{type(tokens)}")
print(f"\n{len(tokens)}")
print(f"\n{tokens[:15]}")

text = nltk.Text(tokens)
text.findall("<BTC>(<.*>)")
text.concordance("BTC")
