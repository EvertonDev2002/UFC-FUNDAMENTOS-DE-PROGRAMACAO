""" Escreva um programa que leia as coordenadas de dois pontos e retorne a distância entre eles. """

from math import sqrt

print("Digite as coordanadas do primeiro ponto")
x1 = float(input("Digite coordanadas de X: ")) 
y1 = float(input("Digite coordanadas de Y: "))

print("Digite as coordanadas do segundo ponto")
x2 = float(input("Digite coordanadas de X: ")) 
y2 = float(input("Digite coordanadas de Y: "))  

print(f"A distância entre os dois pontos é: {sqrt((x2 - x1)**2 + (y2 - y1)**2 )}")

# Fórmulas
# Modo geral: d= R((x2-x1)²+(y2-y1)²)
# Reta paralela ao eixo X: x1-x2
# Reta paralela ao eixo Y: y1-y2