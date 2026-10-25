a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

while b != 0:
    resto = a % b
    a = b
    b = resto

print("El MCD es:", a)