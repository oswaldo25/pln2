import nltk

carpeta_nombre="C:\Users\Sherl\Documents\PNL"
archivo_nombre="texto.txt"
with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto, "spanish")
for token in tokens:
    print(token)

palabras_total=len(tokens)
print ("palabras",palabras_total)

tokens_conjunto=set(tokens)
palabras_diferentes=len(tokens_conjunto)
print("palabras diferentes:",palabras_diferentes)

riqueza_lexica=palabras_diferentes/palabras_total
print("riqueza lexia:", riqueza_lexica)
riqueza_lexicap=100*palabras_diferentes/palabras_total
print("riqueza lexia:", riqueza_lexicap, "%")

texto_nltk=nltk.Text(tokens)
palabra = input("Escribe la palabra a buscar en el documento: ")
texto_nltk.concordance(palabra)
print("-------------------------------------------")
texto_nltk.similar(palabra)
print ("------------------------------------------")
conteo_individual=tokens.count(palabra)
print ("numero de veces que se encuentra la palabra en el texto: ", conteo_individual)
