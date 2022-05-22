import nltk
from urllib import request

url = "https://kevinherrera21.github.io/ComputoNube/nltk.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

tokens = nltk.word_tokenize(raw)
print(f"type: {type(tokens)}")
print(f"Total tokens: {len(tokens)}")
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<NLP>(<.*>)")
text.concordance("NLP")
