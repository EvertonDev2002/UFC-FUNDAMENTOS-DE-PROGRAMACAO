""" Calcule o resultado das expressões, sabendo que A = 5, B = 10, C = – 8 e D = 1.5. """

from math import sqrt
A = 5
B = 10
C = -8 
D = 1.5

#A)
print(f"((2 * {A}) % 3) - ({C}) =", 2 * A % 3 - C,"\n")

#B)
print(f"raiz -2 * {C} / 4 =", sqrt(-2 * C) / 4,"\n")

#C)
print(f"((20 / 3) / 3) + 8² / 2 = ", ((20/3)/3)+ 8**2/2,"\n")

#D)
print(f"5 * 3 + 15 % 5 + 8 – 1 * 20 / 15 = ", A * 3 + 15 % A + 8 - 1 * 20 / 15,"\n")

#E)
print(f"raiz {A}²/4 + {C} x {D} = ",sqrt(A**(A/B)) + C * D,"\n")

#F)
print(f"5² - raiz 125 *  0 / 540 - 10 / 2 = ", 5**2 - sqrt(125) * 0 / 540 - 10 / 2,"\n")