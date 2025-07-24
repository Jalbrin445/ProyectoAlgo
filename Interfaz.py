import tkinter as tk
from tkinter import ttk, messagebox
import variables
import os
from PIL import Image, ImageTk
import unionBase

def InterfazJAMG():
    # Rutas de archivos
    carpeta_principalJAMG = os.path.dirname(os.path.abspath(__file__))
    carpeta_imagenesJAMG = os.path.join(carpeta_principalJAMG, "img")
    RutaUdeAJAMG = os.path.join(carpeta_imagenesJAMG, "Logo_U.png")
    RutaIcono = os.path.join(carpeta_imagenesJAMG, "DeltaHX.ico")

    # Inicialización de datos
    dm = unionBase.inicializar_datos()  # Corregido el nombre de la función

    # Crear ventana principal
    ventanaJAMG = tk.Tk() 
    ventanaJAMG.title(variables.TITULOVENTANA)
    
    # Configurar icono (con manejo de errores)
    try:
        ventanaJAMG.iconbitmap(RutaIcono)
    except:
        print("No se pudo cargar el icono de la ventana")
    
    ventanaJAMG.resizable(True, True)
    ventanaJAMG.config(bg=variables.COLORFONDO)
    ventanaJAMG.geometry(variables.DIMENSIONESVENTANA)
    ventanaJAMG.minsize(800, 600)

    # Marco principal
    MarcoPrincipalJAMG = tk.Frame(ventanaJAMG, bg=variables.COLORFONDO)
    MarcoPrincipalJAMG.pack(fill=tk.BOTH, expand=True)

    # Widgets para sustancia
    entrySustanciaJAMG = ttk.Combobox(
        ventanaJAMG, 
        state="readonly", 
        values=unionBase.lista_sustancias,  # Usar lista_sustancias en lugar de C
        font=("Arial", 12)
    )
    entrySustanciaJAMG.place(relx=0.05, rely=0.07, relwidth=0.15, relheight=0.05)
    entrySustanciaJAMG.set("Agua (g)" if unionBase.lista_sustancias else "No hay datos")
    
    tk.Label(ventanaJAMG, text="Sustancia:", bg=variables.COLORFONDO).place(relx=0.05, rely=0.02)
    tk.Label(ventanaJAMG, text="Estado: g= gaseoso\n y l=liquido", bg=variables.COLORFONDO).place(relx=0.2, rely=0.07)
    # Widgets para temperatura
    entryTinicialJAMG = tk.Entry(ventanaJAMG, bg=variables.COLORFONDO, font=("Arial", 12))
    entryTinicialJAMG.place(relx=0.05, rely=0.20, relwidth=0.1, relheight=0.05)
    tk.Label(ventanaJAMG, text="Temperatura inicial:", bg=variables.COLORFONDO).place(relx=0.05, rely=0.15)
    
    entryTfinalJAMG = tk.Entry(ventanaJAMG, bg=variables.COLORFONDO, font=("Arial", 12))
    entryTfinalJAMG.place(relx=0.25, rely=0.20, relwidth=0.1, relheight=0.05)
    tk.Label(ventanaJAMG, text="Temperatura final:", bg=variables.COLORFONDO).place(relx=0.25, rely=0.15)

    # Widgets para unidad de temperatura
    entryUndT = ttk.Combobox(
        ventanaJAMG, 
        state="readonly", 
        values=["Celsius (°C)", "Kelvin (K)"], 
        font=("Arial", 12)
    )
    entryUndT.place(relx=0.45, rely=0.20, relwidth=0.15, relheight=0.05)
    entryUndT.set("Celsius (°C)")
    tk.Label(ventanaJAMG, text="Unidad de temperatura:", bg=variables.COLORFONDO).place(relx=0.45, rely=0.15)
    

    # Función para manejar selección de sustancia
    def on_sustancia_selected(event):
        sustancia = entrySustanciaJAMG.get()
        if unionBase.cargar_datos_sustancia(sustancia):
            # Actualizar campos con los datos cargados
            entryTinicialJAMG.delete(0, tk.END)
            entryTinicialJAMG.insert(0, str(unionBase.TinicialJAMG))
            
            entryTfinalJAMG.delete(0, tk.END)
            entryTfinalJAMG.insert(0, str(unionBase.TfinalJAMG))
            
            entryUndT.set(unionBase.UnidadTempJAMG)

            # Mensaje de intervalo de temperatura
            messagebox.showinfo("Información", f"El intervalo de temperatura permitido para la sustancia seleccionada es de {unionBase.TinicialJAMG} a {unionBase.TfinalJAMG} {unionBase.UnidadTempJAMG}")
            
            print("Datos cargados correctamente")
        else:
            messagebox.showerror("Error", "No se encontraron datos para esta sustancia")

    entrySustanciaJAMG.bind("<<ComboboxSelected>>", on_sustancia_selected)

    # Función para ajustar tamaño de fuente
    def actualizar_tamano_fuente():
        ancho = ventanaJAMG.winfo_width()
        alto = ventanaJAMG.winfo_height()
        tamanoBase = min(ancho, alto) // 60
        
        for widget in widgetJAMGtxt:
            widget.config(font=("Arial", tamanoBase))

    widgetJAMGtxt = []
    
    def boton_calcular():
        from integral import calculo_entalpia
        calculo_entalpia(entrySustanciaJAMG, entryTinicialJAMG, entryTfinalJAMG, entryUndT)
    # Botón de calcular
    botonCalcularJAMG = tk.Button(
        ventanaJAMG, 
        text="Calcular Entalpía", 
        command=boton_calcular, 
        bg=variables.COLORBOTON, 
        font=("Arial", 12)
    )
    botonCalcularJAMG.place(relx=0.05, rely=0.3, relwidth=0.15, relheight=0.05)
    widgetJAMGtxt.append(botonCalcularJAMG)
    # Cargar imagen del escudo
    try:
        escudoUdeAJAMG = Image.open(RutaUdeAJAMG)
        escudoUdeAJAMG = escudoUdeAJAMG.resize((200, 300), Image.LANCZOS)
        escudo_img = ImageTk.PhotoImage(escudoUdeAJAMG)
        
        contenedor_info = tk.Frame(ventanaJAMG, bg=variables.COLORFONDO)
        contenedor_info.place(relx=0.78, rely=0.2, anchor="n")
        
        tk.Label(contenedor_info, image=escudo_img, bg=variables.COLORFONDO).pack(side=tk.TOP, pady=(0,10))
        
        info_texto = """
            Juan Albrin Meza Guzmán (1)
            Alexander Usuga (2)
            Ingeniería Agroindustrial (1), (2)
            Departamento de Ingeniería Química. Facultad de Ingeniería"""
        
        label_info = tk.Label(contenedor_info, text=info_texto, bg=variables.COLORFONDO, justify="center")
        label_info.pack(side=tk.TOP)
        
        widgetJAMGtxt.append(label_info)
        ventanaJAMG.escudo_img = escudo_img  # Mantener referencia
        
    except Exception as e:
        print(f"Error al cargar imagen: {e}")
        tk.Label(ventanaJAMG, text="No se pudo cargar la imagen", bg=variables.COLORRED).pack()

    ventanaJAMG.bind("<Configure>", lambda event: actualizar_tamano_fuente())
    ventanaJAMG.mainloop()