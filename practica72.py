import nltk
carpeta_nombre="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="Procesamiento de Lenguaje Natural 1.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
print(texto)
print("----------------------------------------------------------------------")
tokens=nltk.word_tokenize(texto, "spanish")
#palabra = input("Escribe la palabra a buscar en el documento: ") 
conteo_individual=tokens.count("procesamiento")
print("numero de veces que se encuentra la palabra en el texto: ", conteo_individual)
palabras_totales=len(tokens)
porcentaje=100*(conteo_individual/palabras_totales)
print("----------------------------------------------------------------------")
print(porcentaje," %")
texto_nltk=nltk.Text(tokens)
print(texto_nltk)

texto_nltk.concordance("procesamiento")
print("----------------------------------------------------------------------")
texto_nltk.similar("procesamiento")
