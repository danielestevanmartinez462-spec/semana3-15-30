import random

secreto = random.randint(1, 10)
intento = int(input("Adivine el numero (1 al 10): "))

while intento != secreto:
    if intento > secreto:
        print("El numero es menor")
    else:
        print("El numero es mayor")
    intento = int(input("Intente otra vez: "))

print("Adivinaste, el numero era", secreto)