import nltk

carpeta_nombre="F:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="Procesamiento de Lenguaje Natural 1.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

palabras_total=len(tokens)
print("palabras", palabras_total)

tokens_conjunto=set(tokens)
palabras_diferentes=len(tokens_conjunto)
print("palabras diferentes:", palabras_diferentes)

riqueza_lexica=palabras_diferentes/palabras_total
print("riqueza lexia:", riqueza_lexica)
riqueza_lexicap=100*palabras_diferentes/palabras_total
print("riqueza lexia:", riqueza_lexicap,"%")

texto_nltk=nltk.Text(tokens) 
lista_palabras=["Instituto","Ley","Elija","ley"]
texto_nltk.dispersion_plot(lista_palabras)

palabra= input("Escribe la palabra a buscar en el documento: ") 
texto_nltk.concordance(palabra)
print("--------------------------------------------")
texto_nltk.similar(palabra)
print("--------------------------------------------")
conteo_individual=tokens.count(palabra)
print("numero de veces que se encuentra la palabra en el texto: ", conteo_individual)
print("--------------------------------------------")
''' palabra2 = input("Escribe la palabra a buscar en el documento: ") 
texto_nltk.concordance(palabra2)
print("--------------------------------------------")
texto_nltk.similar(palabra2)
print("--------------------------------------------")
conteo_individual2=tokens.count(palabra2)
print("numero de veces que se encuentra la palabra en el texto: ", conteo_individual2)
print("--------------------------------------------")
lista_palabras=[palabra1,palabra2]
texto_nltk.dispersion_plot(lista_palabras)
'''