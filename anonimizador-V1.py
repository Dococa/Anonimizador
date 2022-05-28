# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:33:28 2021

Programa que anonimiza a los usuarios de un excel asignandole un código
y permite su reconocimiento mediante dicho código

@author: dococa
"""

import random
import string
import re


salir = False
opcion = 0
 
while not salir:
#menu de inicio

   opcion = input('''
1: Asignar un código a un nombre.
2: Con un código, ver el nombre asignado.
3: Salir del programa.
Seleccione una opción: ''')     


   if opcion == '1':
    
    #Solicitamos el nombre y le asignamos un codigo único
    
        nombre = input ("Indroduzca el nombre a anonimizar: ") 
        codigo_aleatorio = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
        nombre_fichero = "\n" + (codigo_aleatorio) + " = " + (nombre) + " "
        print(nombre_fichero)
        
        
    #Añadimos los datos a un txt
        f = open ('nombres_anonimizados.txt','a+')
        f.write(str(nombre_fichero))
        f.close()

        
   elif opcion == "2":
    
        codigo = input("Introduzca el código: ")
        codigo = codigo.upper()
    #Abre el archivo y lee linea por linea en busca del codigo introducido
     
        lista = []
        def buscaPalabra(str, f):       
            for line in f:        
                for part in line.split():            
                    if str in part:                
                        lista.append(line)
                        strLista = "".join(lista)
                        re.sub("\n$"," ",strLista)
                        return strLista
                
        f = open('nombres_anonimizados.txt','r')
        print ()
        print (buscaPalabra(codigo, f))
        f.close() 

                
   elif opcion == "3":
        salir = True
        
        
   else: 
        print("\nIntroduce una opción correcta")
        