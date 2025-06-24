import pandas as pd
from tkinter import messagebox

# Variables globales
PesoMolecularJAMG = None
FormaJAMG = None
UnidadTempJAMG = None
A = B = C = D = None
TinicialJAMG = TfinalJAMG = None
df = None
lista_sustancias = []

def inicializar_datos():
    global df, lista_sustancias
    try:
        df = pd.read_excel('BASEABC.xlsx', sheet_name='BASEABC')
        lista_sustancias = df["Tipo de sustancia"].tolist()
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar Excel: {e}")
        return False

def cargar_datos_sustancia(sustancia_seleccionada):
    global PesoMolecularJAMG, FormaJAMG, UnidadTempJAMG, A, B, C, D, TinicialJAMG, TfinalJAMG
    
    if df is not None and sustancia_seleccionada in lista_sustancias:
        fila = df[df["Tipo de sustancia"] == sustancia_seleccionada].iloc[0]
        
        PesoMolecularJAMG = fila[2]
        FormaJAMG = fila[4]
        UnidadTempJAMG = fila[5]
        A = fila[6]
        B = fila[7]
        C = fila[8]
        D = fila[9]
        TinicialJAMG = fila[10]
        TfinalJAMG = fila[11]
        
        return True
    return False

# Inicializar datos al importar
inicializar_datos()