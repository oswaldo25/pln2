import nltk
from nltk import word_tokenize
from urllib import request, response

url = "https://github.com/b-guerrero/Natural-Language-Processing/blob/main/doc.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

tokens = word_tokenize(raw)
print(f"\n{type(tokens)}")
print(f"\n{len(tokens)}")
print(f"\n{tokens[:15]}")

text = nltk.Text(tokens)
text.findall("<cabeza>(<.*>)")
text.concordance("cabeza")
