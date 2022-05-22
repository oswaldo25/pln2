'''Jazmin Azucena Gonzalez Peredia / Programa 6 / Parcial 2'''
import nltk 
from nltk import word_tokenize #Tokenización del texto
from urllib import request

url= "https://jazmingope.github.io/pln2/texto1.txt"  #Descarga de un texto
response = request.urlopen(url)
raw = response.read().decode("utf8")

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:15])
text = nltk.Text(tokens)
text.findall("<lenguaje>(<.*>)")
text.concordance("lenguaje")
