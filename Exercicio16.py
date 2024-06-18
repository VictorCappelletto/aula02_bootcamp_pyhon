#Exercicio: Escreva um programa que avalie duas expressões booleanas inseridas pelo 
# usuário e retorne o resultado da operação AND entre elas.

condicao_1=bool(input("insira um nome: "))
condicao_2=bool(input("insira uma idade: "))
cond_final=condicao_1 and  condicao_2
print("Condição de cadastro do cliente: ",cond_final)