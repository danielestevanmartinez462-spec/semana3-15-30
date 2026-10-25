import random

dado = random.randint(1, 6)
print("Salio:", dado)

while dado != 6:
    dado = random.randint(1, 6)
    print("Salio:", dado)

print("Salio un 6, fin del juego")