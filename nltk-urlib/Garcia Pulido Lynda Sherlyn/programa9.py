'''
GARCIA PULIDO LYNDA SHERLYN    6°D   ICI
'''

from tkinter import simpledialog
import nltk
import matplotlib

carpeta_nombre="C:\Users\Sherl\Documents\PNL"

archivo_nombre = "texto.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")

for token in tokens:
    print(token)

palabras_totales = len(tokens)
print("Palabras totales: ", palabras_totales)

print("---------------------------------------------------")

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto)

distribucion.plot()

print("---------------------------------------------------")

hapaxes = distribucion.hapaxes()

for hapax in hapaxes:
    print(hapax)
