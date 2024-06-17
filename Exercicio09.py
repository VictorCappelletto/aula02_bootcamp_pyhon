#Exercicio: Faça um programa que converta a temperatura de Celsius para Fahrenheit.
CONSTANT_FAHRENHEIT=32
temp_celsius=float(input("insira a temperatura em celsius: "))
conv_fahr=temp_celsius*1.8+CONSTANT_FAHRENHEIT
print(f'A temperatura em Fahrenheit é {conv_fahr:.2f} °F')