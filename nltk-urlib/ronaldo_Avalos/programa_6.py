'''Ronaldo Adan Avalos de la mora / Programa 6 / Parcial 2'''
import nltk 
from nltk import word_tokenize #Tokenización del texto
from urllib import request

url= "https://ronaldo-avalos.github.io/pln2/texto.txt"  #Descarga de un texto
response = request.urlopen(url)
raw = response.read().decode("utf8")

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:15])
text = nltk.Text(tokens)
text.findall("<lenguaje>(<.*>)")
text.concordance("lenguaje")
