""" Usando os operadores aritméticos, relacionais e lógicos da linguagem C e supondo que há duas
constantes true e false que simulam valores booleanos, determine os resultados obtidos na
avaliação das expressões lógicas seguintes. 
Obs: Os valores das variáveis são: A = 2, B = 7, C = 3.5 e L = false.
"""

from math import sqrt
a = 2
b = 7
c = 3.5 
l = False

#a
print(b == a * c and l or True)
#b)
print(b > a or b == a**a)
#c)
print(l and b / a >= c or not a <= c)
#d)
print(not l or True and sqrt(a+b) >=c)
#e)
print(l or b**a <= c * 10 + a * b)