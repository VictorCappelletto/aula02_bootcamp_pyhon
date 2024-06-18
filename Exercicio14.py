#Exercicio: Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e,
#em seguida, imprima o dia, o mês e o ano separadamente.

data_user=input("insira uma data no formato dd/mm/aaaa: ")
data_transform=data_user.split("/")
print('Sua data com os campos separados: ')
print(f'dia: {data_transform[0]}')
print(f'mês: {data_transform[1]}')
print(f'ano: {data_transform[2]}')