#Exercicio: Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

condicao_1=bool(input("insira um email: "))
condicao_2=bool(input("insira um cpf: "))
cond_final=condicao_1 or condicao_2
print("Condição de acesso do cliente: ",cond_final)