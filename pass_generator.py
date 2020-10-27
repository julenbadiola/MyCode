#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def main():
	listafechas = []
	listapasswords = []
	lista = []
	casilista = []
	listafinal = []

	#AÑO
	salir = False
	while salir == False:
		anyo = str(input("Año:"))
		if not len(anyo) == 4:
			print("No vale, 4 caracteres")
		else:
			salir = True

	#MES
	salir = False
	while salir == False:
		mes = str(input("Mes:"))
		if not len(mes) == 2:
			print("No vale, 2 caracteres")
		else:
			salir = True

	#DIA
	salir = False
	while salir == False:
		dia = str(input("Día:"))
		if not len(dia) == 2:
			print("No vale, 2 caracteres")
		else:
			salir = True
	barra()
	nombre = str(input("Nombre: ")).lower()
	apellido = str(input("Apellido: ")).lower()
	barra()
	
	#LISTAFECHAS
	salir = False
	while salir == False:
		fecha1 = anyo + mes + dia
		fecha2 = dia + mes + anyo
		fecha3 = dia + mes
		fecha4 = mes + dia
		fecha5 = anyo[2:]
		listafechas.append(fecha1)
		listafechas.append(fecha2)
		listafechas.append(fecha3)
		listafechas.append(fecha4)
		listafechas.append(fecha5)
		salir = True

	#LISTAPASSWORDS
	salir = False
	while salir == False:
		listapasswords.append(nombre + apellido)
		listapasswords.append(apellido + nombre)
		listapasswords.append(nombre.upper())
		listapasswords.append(nombre.capitalize())
		listapasswords.append(nombre.title())
		listapasswords.append(apellido.upper())
		listapasswords.append(apellido.capitalize())
		listapasswords.append(apellido.title())
		listapasswords.append(nombre.upper() + apellido.upper())
		listapasswords.append(nombre.capitalize() + apellido.capitalize())
		listapasswords.append(nombre.title() + apellido.title())
		listapasswords.append(apellido.upper() + nombre.upper())
		listapasswords.append(apellido.capitalize() + nombre.capitalize())
		listapasswords.append(apellido.title() + nombre.title())
		listapasswords.append(nombre[0] + apellido[0])
		listapasswords.append(apellido[0] + nombre[0])
		listapasswords.append(nombre[0].upper() + apellido[0])
		listapasswords.append(nombre[0].upper() + apellido[0].upper())
		listapasswords.append(nombre[0] + apellido[0].upper())
		salir = True

	#LISTA
	salir = False
	while salir == False:
		for e in listafechas:
			for i in listapasswords:
				lista.append(e + i)
				lista.append(i + e)
		salir = True

	exportar(lista, casilista, listafinal)

def exportar(lista, casilista, listafinal):
	
	nombre_archivo = input("Con que nombre exportar y extensión (.txt por defecto): ")
	while len(nombre_archivo) < 2:
		print("Ponle un nombre más largo")
		nombre_archivo = input("Con que nombre exportar y extensión (.txt por defecto): ")

	nombre_archivo_invertido = nombre_archivo[::-1]
	if len(nombre_archivo_invertido) > 3:
		if not nombre_archivo_invertido[3] == "." or nombre_archivo_invertido[4] == ".":
			nombre_archivo = nombre_archivo + ".txt"
	else:
		nombre_archivo = nombre_archivo + ".txt"


	#Las contraseñas deben tener más de 8 caracteres
	#Se quitan también las repetidas
	outfile = open(nombre_archivo, 'w')
	for elemento in lista:
		if len(elemento) > 8: 
			casilista.append(elemento)

	for elemento in casilista:
		if elemento not in listafinal:
			outfile.write('%s\n' % elemento)
			listafinal.append(elemento)
			print(".",end=' ')

	outfile.close()
	print(" ")
	barra()
	print("Creadas %d posibles contraseñas." % len(listafinal))
	barra()

def barra():
	print("-----------------------------------------------------------")

def creditos():
	clear()
	barra()
	print("GENERADOR DE POSIBLES CONTRASEÑAS; Julen Badiola")
	barra()
	print("Crea una lista de posibles contraseñas de una persona a ")
	print("partir de su fecha de nacimiento, nombre y primer apellido.")
	print("2017 - Versión 1.1")
	barra()

if __name__ == '__main__':
	creditos()
	main()