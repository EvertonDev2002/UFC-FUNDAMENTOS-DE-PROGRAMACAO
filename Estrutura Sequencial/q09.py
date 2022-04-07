""" Escreva um programa que leia os coeficientes A, B e C de uma equação Ax²+Bx+C=0 e calcule
o valor do discriminante delta e as raízes da equação. """

from math import sqrt
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))
delta = b**2 - 4 * a * c
print(valido)
bhaskaraMais  = -b + sqrt(delta) / 2 * a
bhaskaraMenos  = -b - sqrt(delta) / 2 * a
print(f"Delta é {delta}\nA raiz da equação é\nX1={bhaskaraMais} e X=2{bhaskaraMenos}")