#Exercicio: Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário
import statistics

numero_1=float(input("insira o primeiro numero: "))
numero_2=float(input("insira o segundo numero : "))
media=statistics.mean([numero_1,numero_2])
print(f'Olá usuário, a média entre os valores é {media:.2f}')