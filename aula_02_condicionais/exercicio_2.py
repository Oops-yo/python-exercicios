"""

Proposta: 2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""

print("Me dê um número")
numero = int(input())

if numero > 0:
    raiz = round(numero ** 0.5 , 2)
    print(f"A raiz quadrada de {numero} é {raiz}")
else:
    print("O número é inválido")

