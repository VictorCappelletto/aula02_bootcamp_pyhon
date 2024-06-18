#Exercicio: Desenvolva um programa que peça ao usuário para inserir uma frase e, 
# em seguida, imprima esta frase sem espaços em branco no início e no final.

frase_user=(input("insira uma frase: "))
frase_sem_espaco=frase_user.strip(" ")
print(f'Sua frase sem espaços: {frase_sem_espaco}')