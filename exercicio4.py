import os
os.system('cls')

numero = int(input("Digite um valor positivo: "))

if numero < 0:
    print("O número é negativo!")
    exit()
else:
    if numero % 2 == 0:
        quadrado = numero ** 2
        print(f"O valor é par. {numero}² = {quadrado:.2f}")
    else:
        cubo = numero ** 3
        print(f"O valor é ímpar. {numero}³ = {cubo:.2f}")