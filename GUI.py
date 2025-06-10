import tkinter as tk
from tkinter import ttk
import variables
import os
from PIL import Image, ImageTk


carpeta_principalJAMG = os.path.dirname(os.path.abspath(__file__))
carpeta_imagenesJAMG = os.path.join(carpeta_principalJAMG, "img")
RutaUdeAJAMG = os.path.join(carpeta_imagenesJAMG, "Logo_U.png")   

ventanaJAMG = tk.Tk() 
ventanaJAMG.title(variables.TITULOVENTANA)
ventanaJAMG.iconbitmap(os.path.join(carpeta_imagenesJAMG, "DeltaHX.ico"))  # Icono de la ventana
ventanaJAMG.resizable(True, True)  # No se puede redimensionar la ventana
ventanaJAMG.config(bg=variables.COLORFONDO)  # Color de fondo de la ventana
ventanaJAMG.geometry(variables.DIMENSIONESVENTANA)  # Ancho y alto de la ventana
ventanaJAMG.minsize(800, 600)  # Tamaño mínimo de la ventana

MarcoPrincipalJAMG = tk.Frame(ventanaJAMG, bg=variables.COLORFONDO)  # Crear un frame para la ventana
MarcoPrincipalJAMG.pack(fill=tk.BOTH, expand=True)  # Empaquetar el frame en la ventana

def actualizar_tamano_fuente():
    anchoJAMG = ventanaJAMG.winfo_width()  # Obtener el ancho de la ventana
    altoJAMG = ventanaJAMG.winfo_height() # Obtener el alto de la ventana

    tamanoBaseJAMG = min(anchoJAMG, altoJAMG) // 60  # Calcular el tamaño de la fuente basado en el tamaño de la ventana
    for widget in widgetJAMGtxt:  # Recorrer todos los widgets de texto
        widget.config(font=("Arial", tamanoBaseJAMG))  # Actualizar el tamaño de la fuente de cada widget
widgetJAMGtxt = []

try:
    escudoUdeAJAMG = Image.open(RutaUdeAJAMG)  # Cargar la imagen del escudo
    escudoUdeAJAMG = escudoUdeAJAMG.resize((200, 300), Image.LANCZOS)  # Redimensionar la imagen
    escudoUdeAJAMG = ImageTk.PhotoImage(escudoUdeAJAMG)  # Convertir la imagen a PhotoImage
    
    contenedor_infoJAMG = tk.Frame(ventanaJAMG, bg=variables.COLORFONDO)  # Crear un frame para el contenedor de la imagen
    contenedor_infoJAMG.place(relx=0.78, rely=0.2, anchor="n")  # Posicionar el frame en la ventana
    labelEscudoUdeAJAMG = tk.Label(contenedor_infoJAMG, image=escudoUdeAJAMG, bg=variables.COLORFONDO)  # Crear un label con la imagen
    labelEscudoUdeAJAMG.pack(side=tk.TOP, pady=(0,10))  # Posicionar el label en la ventana

    nombreEstudianteJAMG = tk.Label(contenedor_infoJAMG, text="Juan Albrin Meza Guzmán (1) \n Alexander Usuga (1) \n Leyder Mausa (1) \n Mario Morelos (2) \n Ingeniería Agroindustrial (1), Ingeniería Bioquímica (2) \n Departamento de Ingeniería Química. Facultad de Ingeniería", bg=variables.COLORFONDO,justify="center",anchor="n")  # Crear un frame para el nombre del estudiante
    nombreEstudianteJAMG.pack(side=tk.TOP)  # Crear un campo de texto para el nombre del estudiante
    widgetJAMGtxt.append(nombreEstudianteJAMG)  # Agregar el widget a la lista de widgets

    entryTinicialJAMG = tk.Entry(ventanaJAMG, bg=variables.COLORFONDO, font=("Arial", 12))  # Crear un campo de texto para la entrada inicial
    entryTinicialJAMG.place(relx=0.05, rely=0.20, relwidth=0.1, relheight=0.05)  # Posicionar el campo de texto en la ventana
    TinicialJAMG = tk.Label(ventanaJAMG, text="Temperatura inicial:", bg=variables.COLORFONDO)  # Crear un label para la entrada inicial
    TinicialJAMG.place(relx=0.05, rely=0.15)  # Posicionar el label en la ventana
    entryTfinalJAMG = tk.Entry(ventanaJAMG, bg=variables.COLORFONDO, font=("Arial", 12))  # Crear un campo de texto para la entrada final
    entryTfinalJAMG.place(relx=0.25, rely=0.20, relwidth=0.1, relheight=0.05)  # Posicionar el campo de texto en la ventana
    TinicialJAMG = tk.Label(ventanaJAMG, text="Temperatura final:", bg=variables.COLORFONDO)  # Crear un label para la entrada inicial
    TinicialJAMG.place(relx=0.25, rely=0.15)  # Posicionar el label en la ventana
    
    entryUndT = tk.ttk.Combobox(ventanaJAMG, state="readonly", values=["Celsius (°C)", "Kelvin (K)"], font=("Arial", 12))  # Crear un combobox para la unidad de temperatura
    entryUndT.place(relx=0.45, rely=0.20, relwidth=0.15, relheight=0.05)  # Posicionar el combobox en la ventana
    entryUndT.set("Celsius (°C)")  # Establecer el valor por defecto del combobox
    UndTLabelJAMG = tk.Label(ventanaJAMG, text="Unidad de temperatura:", bg=variables.COLORFONDO)  # Crear un label para la unidad de temperatura
    UndTLabelJAMG.place(relx=0.45, rely=0.15)  # Posicionar el label en la ventana
    
    entrySustanciaJAMG = tk.ttk.Combobox(ventanaJAMG, state="readonly", values=["Agua (g)", "Agua (l)"], font=("Arial", 12))  # Crear un combobox para la sustancia
    entrySustanciaJAMG.place(relx=0.05, rely=0.07, relwidth=0.15, relheight=0.05)  # Posicionar el combobox en la ventana
    entrySustanciaJAMG.set("Agua (g)")  # Establecer el valor por defecto del combobox
    SustanciaLabelJAMG = tk.Label(ventanaJAMG, text="Sustancia:", bg=variables.COLORFONDO)  # Crear un label para la sustancia  
    SustanciaLabelJAMG.place(relx=0.05, rely=0.02)  # Posicionar el label en la ventana
    widgetJAMGtxt.extend([entryTinicialJAMG, entryTfinalJAMG, entryUndT, entrySustanciaJAMG])  # Agregar los widgets a la lista de widgets
except:
    tk.Label(ventanaJAMG, text="No se pudo cargar la imagen del escudo", bg=variables.COLORRED).pack()

ventanaJAMG.bind("<Configure>", lambda event: actualizar_tamano_fuente())  # Actualizar el tamaño de la fuente al redimensionar la ventana
ventanaJAMG.mainloop()