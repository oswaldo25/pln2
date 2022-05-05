# -*- coding: utf-8 -*-
'''
El ejercicio consiste en en:
- Contar las lÃ­neas que tiene un archivo y mostrar el nÃºmero junto a cada lÃ­nea
- Mostrar el contenido de cada lÃ­nea, y en caso de que estÃ© vacÃ­a, indicar en pantalla que la lÃ­nea esta vacÃ­a.
- Mostrar en pantalla un conteo final indicando cuÃ¡ntas lÃ­neas son en total, cuÃ¡ntas tienen texto y cuÃ¡ntas no.
'''
carpeta_nombre="F:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="acuerdo.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

palabra = input("Escribe la palabra a buscar en el documento: ") 
num_palabras=0
num_linea=1
num_texto=0
num_vacio=0
for linea in lineas_lista:
	if linea.strip() == "":
		num_linea=num_linea+1
		print("LINEA",num_linea,":","Esta línea está vacía")
		num_vacio=num_vacio+1
	else:
		num_linea=num_linea+1
		print("LINEA",num_linea,":",linea)
		num_texto=num_texto+1
		if palabra in linea:
			num_palabras = num_palabras+1
print("Lineas totales:",num_linea)
print("Lineas con texto:",num_texto)
print("Lineas vacías:",num_vacio)
print("la palabra:",palabra,"se encuentra:",num_palabras,"veces en el documento")