""" Escreva um programa que leia as coordenadas (x,y) de um ponto e retorne a sua distância até a
origem do sistema de coordenadas. """

from math import sqrt
x = float(input("Digite coordanadas de X: ")) 
y = float(input("Digite coordanadas de Y: ")) 
print(f"A distância até a origem é: {sqrt(x**2 + y**2)}")