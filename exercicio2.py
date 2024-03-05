import os
os.system('cls')

nome1 = input("Digite o nome da primeira pessoa: ")
nome2 = input("Digite o nome da segunda pessoa: ")
peso1 = float(input("Digite o peso da primeira pessoa: "))
peso2 = float(input("Digite o peso da segunda pessoa: "))

if peso1 == peso2:
    print(f"{nome1} e {nome2} tem o mesmo peso. Peso = {peso1}")
else:
    if peso1 > peso2:
        print(f"{nome1}, com {peso1}KG é mais pesado que {nome2}, com {peso2}KG")
    elif peso2 > peso1:
        print(f"{nome2}, com {peso2}KG é mais pesado que {nome1}, com {peso1}KG")