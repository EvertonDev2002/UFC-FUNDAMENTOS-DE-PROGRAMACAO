""" Faça um programa que leia um número inteiro positivo de 4 dígitos e imprima 1 dígito por
linha. """

inteiro = int(input("Digite um número com 4 dígitos: ")) 
print(f" Milhar: {inteiro//1000 % 10}\n Centena: {inteiro//100 % 10}\n Dezena: {inteiro//10 % 10}\n Unidade: {inteiro//1 % 10}")