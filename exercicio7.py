import os
os.system('cls')

rg = int(input("Digite o RG do empregado (sem . e sem -): "))
anoNasc = int(input("Digite o ano de nascimento do empregado: "))
anoInicial = int(input("Digite o ano de ingresso na empresa: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNasc
tempoTrabalho = anoAtual - anoInicial

if idade >= 65:
    print(f"A idade do funcionário é: {idade}. Requerer Aposentadoria!")
elif tempoTrabalho >= 30:
    print(f"O tempo de trabalho é: {tempoTrabalho}. Requerer Aposentadoria!")
elif idade >= 60 and tempoTrabalho >= 25:
    print(f"A idade é {idade} e o tempo de trabalho é {tempoTrabalho}. Requerer Aposentadoria!")
else:
    print("Não requerer Aposentadoria!")