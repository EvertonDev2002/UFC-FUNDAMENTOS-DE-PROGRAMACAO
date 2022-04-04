""" Faça um programa que leia um número inteiro positivo de três dígitos e imprima o número
formado pelos dígitos invertidos do número lido. Ex: Número lido = 123 → Número escrito = 321. """

inteiro = int(input("Digite um número com 3 dígitos: ")) 
print(f" Número lido:{inteiro}\n Invertido:{inteiro//1 % 10}{inteiro//10 % 10}{inteiro//100 % 10}")