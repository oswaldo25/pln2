carpeta_nombre="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="acuerdo.txt"
palabra = input("Escribe la palabra a buscar en el documento: ") 
'''
palabra1="acuerdo"
palabra2="RESOLUCIÃ“N"
'''
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

if palabra in texto:
	print("la palabra:", palabra, " fue encontrada en el texto")
else:
	print("la palabra:", palabra, " no fue encontrada en el texto")

