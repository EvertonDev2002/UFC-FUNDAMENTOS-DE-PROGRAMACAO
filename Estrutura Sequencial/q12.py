"""  Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula da conversão é
R=G⋅(π /180) , sendo G o ângulo em graus e R em radianos. (Obs: defina uma constante para o
valor de π ). """

from math import pi
graus = float(input("Valor em gruas: "))
radianos = graus * (pi/180)
print("%.6f" % radianos)