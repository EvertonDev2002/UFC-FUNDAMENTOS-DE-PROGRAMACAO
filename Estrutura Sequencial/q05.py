"""  Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como
taxa de câmbio US$ 1,00 = R$ 3,92. Leia um valor em Dólares pelo teclado e mostre o
correspondente em Reais. """

dolar = float(input("Digite o valor em dólar: "))
cambio = 3.92
print(f"US$ {dolar} em real é R$ {dolar * cambio}")