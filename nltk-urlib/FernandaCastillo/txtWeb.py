''' Fernada Castillo '''

'''
Tokenizacion del texto
'''
import nltk
from nltk import word_tokenize

from urllib import request
'''
Descarga de un texto
'''

url="https://github.com/FerCDD/PLN_prueba/blob/gh-pages/NLTK.txt"
response=request.urlopen(url)
raw=response.read().decode('utf8')

tokens=word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:15])

text=nltk.Text(tokens)
text.findall("<NLTK><.*>")
text.concordance("NLTK")