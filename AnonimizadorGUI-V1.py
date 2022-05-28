# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:33:28 2021

Programa que anonimiza a los usuarios asignandole un código
y permite su identificación mediante dicho código.

@author: D0c0c4 
"""
#librerias necesarias
import random
import string
import re
from tkinter import *
 

#configuración de la ventana pricipal
ventana = Tk()
ventana.title ("Anonymizador")
ventana.geometry("{0}x{1}".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
#ventana.iconbitmap(r'C:\Users\dcoll\Desktop\FAVICON.ico')
ventana['bg'] = 'light blue'

bienvenida = Label(ventana, text="¡Bienvenido a Anonymizador!\n", font=("Helvetica", 26), bg="lightblue")
bienvenida.pack()

#Creamos y desplegamos los frames que vamos a utilizar
frame1 = Frame(ventana, bg="lightblue",relief=RAISED,borderwidth=2)
frame1.pack()
frame2 = Frame(ventana, bg="lightblue")
frame2.pack()
frame3 = Frame(ventana, bg="lightblue")
#frame3.pack()
frame4 = Frame(ventana, bg="lightblue")
#frame4.pack()


que_opcion = Label(frame1, text="¿Qué desea hacer?", font=("Helvetica", 18), bg="lightgreen",relief=RAISED,borderwidth=1)
que_opcion.grid(column=0, row=0, sticky = NSEW)
    
name_var = StringVar()
nombre_fichero = StringVar()

code_var = StringVar()
codigo=StringVar()
lista=[]

def submit_name():  #Botón de la opción 1
 
     #genera el codigo y almacena los datos en nombres_anonimizados.txt
    
     nombre=name_var.get()
     
     if name_var.get()=="":
            messagebox.showerror(message="No puede dejar el cuadro de entrada vacio", title="Error")
            return
     name_var.set("") 
     
        
     codigo_aleatorio = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
     nombre_fichero = "\n" + "  "*20 + (codigo_aleatorio) + " = " + (nombre) + "  "*20
     
     
     frame4.pack_forget()
     frame3.pack_forget()
     frame3.pack()
     output_name_label = Label(frame3, text = nombre_fichero, font=("Helvetica", 18),bg="lightblue")
     output_name_label.grid(column=0, row=0, ipadx=10, ipady=10)
     
    #Añadimos los datos a un txt
     f = open ('nombres_anonimizados.txt','a+')
     f.write(str(nombre_fichero))
     f.close()
        
def generar_codigo():  #Solicitamos el nombre y le asignamos un codigo único. Opcion 1
    
    name_label = Label(frame2, text = '         Nombre:      ', font=("Helvetica", 18),bg="lightblue")
    name_entry = Entry(frame2  ,textvariable = name_var, font = ("Helvetica", 18))
    sub_btn=Button(frame2,text = 'Enviar', command = submit_name, font = ("Helvetica", 11))
    
    name_label.grid(column=0, row=0 ,sticky = W)
    name_entry.grid(column=1, row=0 ,sticky = W)
    sub_btn.grid(column=2, row=0)
    
    
 
    

def submit_code():  #Botón de la función 2
    
    
    codigo=code_var.get()
    
    if code_var.get()=="":
        messagebox.showerror(message="No puede dejar el cuadro de entrada vacio", title="Error")
        return
    code_var.set("")
    strLista=""
    
    
    f = open('nombres_anonimizados.txt','r')
    #Abre el archivo y lee linea por linea en busca del codigo introducido
    
    for line in f:   
        for part in line.split():            
            if str(codigo) in part:                
                lista.append(line)
                strLista = "".join(lista)
                re.sub("\n$"," ",strLista)
                
    if lista == []:
        messagebox.showinfo(message="El nombre o código introducido no se corresponde con ningún usuario", title="Error")
                
    f.close()
      
    frame3.pack_forget()
    frame4.pack_forget()
    frame4.pack()
    output_code_label = Label(frame4, text = " "*10 + strLista + " "*10, font=("Helvetica", 18),bg="lightblue")
    output_code_label.grid(column=0, row=0, ipadx=20, ipady=20)  
    
    lista.clear()
    
    
    
def consultar_nombre():  #Solicitamos el nombre y le asignamos un codigo único. Opcion 2
    
    
    name_label = Label(frame2, text = 'Código o Nombre: ', font=("Helvetica", 18),bg="lightblue")
    name_entry = Entry(frame2  ,textvariable = code_var, font = ("Helvetica", 18))
    sub_btn=Button(frame2,text = 'Enviar',command = submit_code , font = ("Helvetica", 11))
    
     
    name_label.grid(column=0, row=0 ,sticky = W)
    name_entry.grid(column=1, row=0 ,sticky = W)
    sub_btn.grid(column=2, row=0)      
    
    
def salida():  #Función que sale de la app. Opción 3
     ventana.destroy()
    
    
        
     
#Creamos y desplegamos los botones radales de las 3 funciones principales
opt1 = Radiobutton(frame1,text=' Generar código aleatorio para un nombre.                      ',value=0, font=("Helvetica", 14), bg="lightblue", command = generar_codigo)
opt2 = Radiobutton(frame1,text=' Consultar el nombre asignado a un código o viceversa.', value=1, font=("Helvetica", 14), bg="lightblue", command = consultar_nombre)
opt3 = Radiobutton(frame1,text=' Salir.                                                                                    ', value=2, font=("Helvetica", 14), bg="lightblue", command = salida)

opt1.grid(column=0, row=1 ,sticky = W)
opt2.grid(column=0, row=2, sticky = W)
opt3.grid(column=0, row=3, sticky = W)

ventana.mainloop()

