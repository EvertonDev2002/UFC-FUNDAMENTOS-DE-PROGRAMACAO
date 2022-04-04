""" Escreva um programa que leia a altura e o raio da base de um cilindro circular reto e escreva as
seguintes informações: área lateral, área da base e volume. """

from math import pi
altura = float(input("Digite a altura: "))
raioDaBase = float(input("Digite o raio da base: "))
areaBase = pi * raioDaBase**2
areaLateral = 2*pi * raioDaBase * altura
volume = areaBase * altura
print(f" área lateral: {(areaLateral)/pi}π cm²\n área da base: {(areaBase)/pi}π cm²\n volume: {(volume)/pi}π cm²")