from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox
from pathlib import Path

#The place where we are going to save the file
downloaso = str(Path.home() / "Downloads")

#-------------------------

print(os.getcwd())

#Making the definition of the download action 
def accion():
    enlace=videos.get()     
    video = YouTube(enlace)  
    descarga = video.streams.get_highest_resolution()
    descarga.download(downloaso)

#Designing the window
root = Tk()
root.config(bd=15)
root.title("Dobe")
root.resizable(False,False)
root.iconbitmap('favicon.ico')

#Designing the UI (interface)
instrucciones = Label(root, text="Ingresa el link del vídeo para descargarlo")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

#-------------------------

root.mainloop()
