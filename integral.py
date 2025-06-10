import sympy as sy
import sys


salir = False
while not salir:
    sustancia = input("Ingresa el nombre de una sustancia a la cual le deseas / encontrar su capacidad calorifica por ejemplo: Agua (g)")
    if sustancia.lower() == "agua l":
        print("El rango de temperatura permitido es de 0-100 °C")
    elif sustancia.lower() == "agua g":
        print("El rango de temperatura permitido es de: 0-1500")
    T1 = float(input("Ingresa por favor el primer valor de la temperatura: "))
    T2 = float(input("Ingresa por favor el valor final de la temperatura: "))
    UndT = input("Ingresa por favor la unidad de temperatura Kelvin (K) o Celsius (°C): ")
    if sustancia.lower() == "agua g":
        if (T1 >= 0 and T2 <= 1800) and UndT.upper() == "C":
            a, b, c, d = 33.46,0.6880,0.7604,-3.593
            forma = 1
        elif (T1 >= 0 and T2 <= 1800) and UndT.upper() == "K":
            T1 = T1 - 273.15
            T2 = T2 - 273.15
            a, b, c, d = 33.46,0.6880,0.7604,-3.593
            forma = 1
        else:
            print("No ingresaste un valor valido entre el rango de temperatura para la sustancia indicada o no tomaste en cuenta las dos unidades de temperatura, vuelve a ingresar")
            continue

    elif sustancia.lower() == "agua l":
        if UndT.upper() == "C":
            a, b, c, d = 75.4, 0, 0, 0
            forma = 1
        elif UndT.upper() == "K":
            T1 = T1 - 273.15
            T2 = T2 - 273.15
            a, b, c, d = 75.4, 0, 0, 0
            forma = 1
    else:
        print("Ingresa una sustancia correcta.")
        continue

    T = sy.symbols("T")

    if forma == 1:
        resultado1 = sy.integrate((a*(10**(-3))) + (b*(10**(-5)))*T + (c*(10**(-8)))*T**2 + (d*(10**(-12)))*T**3)
        resultado2 = sy.integrate(((a*(10**(-3))) +(b*(10**(-5)))*T + (c*(10**(-8)))*T**2 + (d*(10**(-12)))*T**3), (T, T1, T2))

    elif forma == 2:
        resultado1 = sy.intagrate((a*(10**(-3))) +(b*(10**(-5)))*T + (c*(10**(-8)))*T**-2)
        resultado2 = sy.intagrate(((a*(10**(-3))) +(b*(10**(-5)))*T + (c*(10**(-8)))*T**-2), (T, T1, T2))

    if resultado2 != 0:
        print(f"el valor del cambio de entalpia para el {sustancia} entre un intervalo de {T1} - {T2} {UndT} es de = {resultado2} Kj/mol*°C")
        print(f"la integrar es: {resultado1}")
    salir = int(input("Usted desea seguir (escriba 0 para continuar y 1 o cualquier otro numero para no continuar: "))
