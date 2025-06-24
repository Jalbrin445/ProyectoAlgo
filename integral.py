import sympy as sy
import sys
import unionBase



T = sy.symbols("T")

if unionBase.FormaJAMG == 1:
    resultado1 = sy.integrate((unionBase.A*(10**(-3))) + (unionBase.B*(10**(-5)))*T + (unionBase.C*(10**(-8)))*T**2 + (unionBase.D*(10**(-12)))*T**3)
    resultado2 = sy.integrate(((unionBase.A*(10**(-3))) +(unionBase.B*(10**(-5)))*T + (unionBase.C*(10**(-8)))*T**2 + (unionBase.D*(10**(-12)))*T**3), (T, unionBase.TfinalJAMG, unionBase.TfinalJAMG))

elif unionBase.FormaJAMG == 2:
    resultado1 = sy.intagrate((unionBase.A*(10**(-3))) +(unionBase.B*(10**(-5)))*T + (unionBase.C*(10**(-8)))*T**-2)
    resultado2 = sy.intagrate(((unionBase.A*(10**(-3))) +(unionBase.B*(10**(-5)))*T + (unionBase.C*(10**(-8)))*T**-2), (T, unionBase.TinicialJAMG, unionBase.TfinalJAMG))

if resultado2 != 0:
    print(f"el valor del cambio de entalpia para el entre un intervalo de {unionBase.TfinalJAMG} - {unionBase.TfinalJAMG} {unionBase.UnidadTempJAMG} es de = {resultado2} Kj/mol*°C")
    print(f"la integrar es: {resultado1}")
salir = int(input("Usted desea seguir (escriba 0 para continuar y 1 o cualquier otro numero para no continuar: "))
