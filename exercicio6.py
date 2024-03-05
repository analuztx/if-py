import os
os.system('cls')

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

print("MENU")
print("1. Média Ponderada, com pesos 2 e 3, respectivamente.")
print("2. Quadrado da soma dos 2 números.")
print("3. Cubo do menor número.")

opcao = int(input("Digite uma opção: "))

if opcao == 1:
    mediaPonderada = (num1 * 2 + num2 * 3)/5
    print(f"A média ponderada dos valores {num1} e {num2} é = {mediaPonderada}")
elif opcao == 2:
    soma = num1 + num2
    quadradoSoma = soma ** 2
    print(f"O quadrado da soma dos dois valores é = {quadradoSoma}")
elif opcao == 3:
    if num1 < num2:
        cuboMenor = num1 ** 3
        print(f"O cubo do menor valor {num1} é = {cuboMenor}")
    elif num2 < num1:
        cuboMenor = num2 ** 3
        print(f"O cubo do menor valor {num2} é = {cuboMenor}")
    elif num1 == num2 and num2 == num1:
        print("Os valores são iguais.")
else:
    print("Opção inválida! Tente novamente.")
    exit()