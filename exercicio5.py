import os
os.system('cls')

altura1 = float(input("Digite a altura 1: "))
altura2 = float(input("Digite a altura 2: "))
altura3 = float(input("Digite a altura 3: "))

if altura1 >= altura2 >= altura3:
    print(f"{altura1}, {altura2}, {altura3}")
elif altura1 >= altura3 >= altura2:
    print(f"{altura1}, {altura3}, {altura2}")
elif altura2 >= altura1 >= altura3:
    print(f"{altura2}, {altura1}, {altura3}")
elif altura2 >= altura3 >= altura1:
    print(f"{altura2}, {altura3}, {altura1}")
elif altura3 >= altura1 >= altura2:
    print(f"{altura3}, {altura1}, {altura2}")
elif altura3 >= altura2 >= altura1:
    print(f"{altura3}, {altura2}, {altura1}")

elif altura1 >= altura2 <= altura3:
    print(f"{altura3}, {altura1}, {altura2}")
elif altura1 <= altura2 >= altura3:
    print(f"{altura2}, {altura1}, {altura3}")

elif altura2 >= altura1 <= altura3:
    print(f"{altura3}, {altura2}, {altura1}")
elif altura2 <= altura1 >= altura3:
    print(f"{altura1}, {altura2}, {altura3}")

elif altura3 >= altura1 <= altura2:
    print(f"{altura2}, {altura3}, {altura1}")
elif altura3 <= altura1 >= altura2:
    print(f"{altura1}, {altura3}, {altura2}")