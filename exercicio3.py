import os
os.system('cls')

sexo = input("Digite o sexo (F/M): ")
altura = float(input("Digite a altura (em M): "))

if sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {pesoIdeal:.2f}")
elif sexo == 'M':
    pesoIdeal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {pesoIdeal:.2f}")
