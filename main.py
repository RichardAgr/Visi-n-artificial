import tkinter as tk
from tkinter import Label
import subprocess
import json
import os

personaDesaparecida = ""
cantPersonas=0;
anchoVentana = 300
altoVenteana = 400

nombre = "nombre.json"

def entrenarModelo():
    subprocess.run(["python", "Entrenador.py"])
    
def buscarPersona():
    subprocess.run(["python", "Reconocedor_Facial.py"])

def escribirNombre():
    with open(nombre, "w") as archivoConfiguracion:
         json.dump({cantPersonas: personaDesaparecida}, archivoConfiguracion)
    
    subprocess.run(["python", "Capturador_Rostros.py"])
   
def centrarVentana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
    
def registro():
    registroVentana = tk.Toplevel()
    registroVentana.title("Registrar Persona Desaparecida")
    registroVentana.geometry("300x200")
    
    centrarVentana(registroVentana, 300, 200)
    
    label = tk.Label(registroVentana, text="Nombre de la persona:")
    label.pack(pady=10)
    
    entradaNombre = tk.Entry(registroVentana, width=30)
    entradaNombre.pack(pady=10)
    
    botonGuardar = tk.Button(registroVentana, text="Guardar", command=lambda: guardarNombre(entradaNombre.get(),registroVentana))
    botonGuardar.pack(pady=10)

def guardarNombre(nombre, ventana):
    global personaDesaparecida
    personaDesaparecida = nombre
    cantPersonas+1;
    escribirNombre()
    ventana.destroy()
    

    
ventana = tk.Tk()
ventana.geometry("300x400+200+30")
ventana.title("Sistema de Busqueda de Personas")
ventana.resizable(width=False,height=False)

frame = tk.Frame(ventana)
frame.pack(expand=True)
#botones
boton = tk.Button(frame, text="Registrar persona desaparecida",bg="#D4DCDA",cursor="hand2",
                  width=15, height=3,font=("Arial",12,"bold"), wraplength=200,command=registro)
boton.pack(pady=10)

boton2 = tk.Button(frame,text="Entrenar Modelo",bg="#D4DCDA",cursor="hand2",
                  width=15, height=3,font=("Arial",12,"bold"),command=entrenarModelo)
boton2.pack(pady=10)

boton2 = tk.Button(frame,text="Buscar persona (Finaliza ESC)",bg="#D4DCDA",cursor="hand2",
                  width=15, height=3,font=("Arial",12,"bold"),wraplength=180,  command=buscarPersona)
boton2.pack(pady=10)

centrarVentana(ventana,anchoVentana,altoVenteana)
ventana.mainloop()