import sympy as sy
from tkinter import messagebox
import unionBase

def calculo_entalpia(entrySustanciaJAMG, entryTinicialJAMG, entryTfinalJAMG, entryUndT):
    try:
        # Obtener valores de los campos
        sustancia = entrySustanciaJAMG.get()
        Tinicial = float(entryTinicialJAMG.get())
        Tfinal = float(entryTfinalJAMG.get())
        unidad_temp = unionBase.UnidadTempJAMG
        unidad_temp = entryUndT.get()
        
        # Validar datos básicos
        if not sustancia or unidad_temp not in ["Celsius (°C)", "Kelvin (K)"]:
            messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
            return
        # Verificar que se hayan cargado los datos de la sustancia
        if not unionBase.cargar_datos_sustancia(sustancia):
            messagebox.showerror("Error", "No se encontraron datos para esta sustancia.")
            return
        # Convertir temperaturas
        if unidad_temp == "Celsius (°C)" and unionBase.UnidadTempJAMG == "Kelvin (K)":
            Tinicial += 273.15
            Tfinal += 273.15
            unidad_temp = "Celsius (°C)"
        elif unidad_temp == "Kelvin (K)" and unionBase.UnidadTempJAMG == "Celsius (°C)":
            Tinicial -= 273.15
            Tfinal -= 273.15
            unidad_temp = "Kelvin (K)"
        if unidad_temp == "Kelvin (K)":
            und_Ent = "Kj/mol*K"
        elif unidad_temp == "Celsius (°C)":
            und_Ent = "Kj/mol*°C"
        # Validar rango de temperatura
        if Tinicial < unionBase.TinicialJAMG or Tfinal > unionBase.TfinalJAMG:
            messagebox.showerror("Error", 
                f"Temperaturas fuera de rango. El intervalo permitido es: {unionBase.TinicialJAMG} a {unionBase.TfinalJAMG} {unidad_temp}")
            return
        
        T = sy.symbols("T")

        if unionBase.FormaJAMG == 1:
            resultado1 = sy.integrate((unionBase.A*(10**(-3))) + (unionBase.B*(10**(-5)))*T + (unionBase.C*(10**(-8)))*T**2 + (unionBase.D*(10**(-12)))*T**3, T)
            resultado2 = sy.integrate((unionBase.A*(10**(-3))) + (unionBase.B*(10**(-5)))*T + (unionBase.C*(10**(-8)))*T**2 + (unionBase.D*(10**(-12)))*T**3, (T, Tinicial, Tfinal))

        elif unionBase.FormaJAMG == 2:
            resultado1 = sy.integrate(round((unionBase.A*(10**(-3)),2)) + (round(unionBase.B*(10**(-5)), 2))*T + (round(unionBase.C*(10**(-8)), 2))*T**-2, T)
            resultado2 = sy.integrate((unionBase.A*(10**(-3))) + (unionBase.B*(10**(-5)))*T + (unionBase.C*(10**(-8)))*T**-2, (T, Tinicial, Tfinal))

        if resultado2 != 0:
            # Verificar si el resultado es numérico
            if not sy.core.numbers.Float(resultado2).is_finite:
                messagebox.showerror("Error", "El cálculo produjo un resultado no numérico. Verifique los datos de entrada.")
                return
                
            # Formatear el resultado solo si es numérico
            resultado_formateado = f"{float(resultado2):.4f}" if sy.core.numbers.Float(resultado2).is_finite else "No calculable"
            
            messagebox.showinfo("Resultado", 
                f"Cambio de entalpía para {sustancia}\n"
                f"Peso Molecular (g/mol): {unionBase.PesoMolecularJAMG}\n"
                f"Intervalo: {entryTinicialJAMG.get()} - {entryTfinalJAMG.get()} {unidad_temp}\n"
                f"Resultado: {resultado_formateado} {und_Ent}\n"
                f"Integral indefinida: {resultado1}")

    except ValueError as e:
        messagebox.showerror("Error", f"Error en los datos ingresados: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {str(e)}")