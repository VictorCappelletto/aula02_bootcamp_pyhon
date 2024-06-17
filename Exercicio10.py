#Exercicio: Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

raio=float(input("insira o valor do raio em cm: "))
area_circ=math.pi*raio**2
print(f'A área do círculo é {area_circ:.2f} cm2')
