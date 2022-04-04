""" O imposto brasileiro sobre acessórios de video-games é de 40%. Escreva um programa que leia
o valor de um acessório e retorne a quantia repassada ao governo por imposto. """

valor = float(input("Digite o valor do acessório: "))
print(f"{(40/100) * valor }")

# Fórmula
# porcentagem / 100 * valor 
# Converte a porcentagem em fração e depois multiplique pelo valor 