from tkinter import *
import tkinter
import os
import threading
from tkinter import messagebox, filedialog
import os
import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from tkinter.constants import INSERT
from PIL import Image
p1 = tkinter.Tk()
p1.title("Conversor de archivos")
p1.configure(background="gray40")
p1.geometry("1200x600")
p1.resizable(width=False, height=False)
audio = ""
var = tk.StringVar()
ruta = tk.StringVar()
ruta_salida = tk.StringVar()
var_salida = tk.StringVar()
ty = ""
file = ""

formatos = [".mp3",".mp4",".wav",".ogg",".flv",".aiff",".mp2",".au",".m4a"]
def abrirArchivo():
    file = filedialog.askopenfilename(initialdir = "/", title = "Selecciona el export JIRA",filetypes = (("Ficheros excel","*.xlsx"),("Macros","*.xlsm"),("All files","*.*")))
    var.set(file)
    ruta.set(file)
def definir_Ruta():
    file = filedialog.askdirectory(initialdir = "/", title = "Selecciona a donde ira a parar el archivo convertido")
    var_salida.set(file)
    ruta_Salida.set(file)
def p2():
    p2 = tkinter.Tk()
    p2.title("Conversor de Videos")
    p2.configure(background="gray40")
    p2.geometry("600x300")
    p2.resizable(width=False, height=False)
def p3():
    pass

#Botones P1



Archivo_Entrada = Button(p1, text="Archivo Base", command=abrirArchivo).place(x=10,y=10)
ruta_Entrada = Entry(p1, textvariable=ruta,state='disabled').place(x=10,y=40)
archivo_Salida = tk.Button(p1, text="Ruta de salida", command=definir_Ruta).place(x=10,y=80)
ruta_Salida = Entry(p1, textvariable=ruta_salida,state='disabled').place(x=10,y=120)
Video = tk.Button(p1,text="Videos",command=p2)
Audio = tk.Button(p1,text="Audios",command=p3)

Video.pack()
Audio.pack()

p1.mainloop()
