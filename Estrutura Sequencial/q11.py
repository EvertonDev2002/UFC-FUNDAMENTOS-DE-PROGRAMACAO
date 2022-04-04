""" Escreva um programa que leia os dois catetos de um triângulo retângulo e retorne o valor da
hipotenusa. """

from math import sqrt
catetoOposto = float(input("Cateto Oposto: "))
catetoAdjacente = float(input("Cateto Adjacente: "))
print(f"O valor da hipotenusa é: {sqrt(catetoOposto**2 + catetoAdjacente**2)} ")