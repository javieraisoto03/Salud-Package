"""Programa que calcula el IMC de una persona de acuerdo a su peso y su altura.
Luego, su nivel de peso corresponde a:
     IMC           CLASIFICACIÓN
----------------------------------
   < 18.5      ->   Peso bajo
 18.5 - 24.9   ->   Peso normal
 25.0 - 29.9   ->   Sobrepeso
 30.0 - 39.9   ->   Obesidad
   > 40.0      ->   Obesidad morbida

IMC = peso / (estatura * estatura)
"""
#Con este código, importamos los módulos "moduloIMC.py" y "moduloRC.py", que pueden ser llamados usando el archivo vacio "__init__.py"

import moduloIMC as imc
import moduloRC as rc

#Cálculo del IMC (Índice de masa corporal)
p = float(input("Ingrese el peso (Kg): "))
a = float(input("Ingrese la altura (m): "))
im= imc.calcularIMC(p,a)
print("Su nivel de peso es:", im)

#Cálculo del rendimiento cardiaco de una persona
e = int(input("Ingrese la edad (años): "))
pj = int(input("Ingrese el porcentaje de la capacidad máxima: "))
r=rc.calcularR(e,pj)
print("Su nivel de rendimiento cardiaco es:", r)
