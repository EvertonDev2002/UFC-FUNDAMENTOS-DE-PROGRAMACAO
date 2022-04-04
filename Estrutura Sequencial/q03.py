""" Suponha que o símbolo ÷ divide dois números e retorna o número inteiro resultado da divisão
sem a parte fracionária e o símbolo / divide dois números e retorna um valor real com a resposta
exata. Ambos os operadores possuem a mesma precedência. Sabendo que os valores das variáveis
são X = – 1, Y = 3 e Z = 7, calcule os resultados das seguintes atribuições. """

x = -1
y = 3
z = 7
media = [
    (x + y + z) / 3,
    x + y + z / 3
]

k = [
    z % y / 3,
    (z / y / 3),
    z % (y/3)
]

# A)
print("Y = Y + 1 | ", y + 1,"\n")
# B)
print("Y = Y + 3 | ", y + 3,"\n")
# C)
print("Media = ( X + Y + Z ) / 3 | ", media[0],"\n")
# D)
print("Media = X + Y + Z / 3 | ", media[1],"\n")
# E)
print("K = Z ÷ Y / 3 | ", k[0],"\n")
# F)
print("K = ( Z ÷ Y ) / 3 | ", k[1],"\n")
# G)
print("K= Z ÷ (Y /3) | ", k[2],"\n")
