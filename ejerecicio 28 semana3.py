numero = int(input("Ingrese un numero entero positivo: "))
divisores = 0
i = 1

while i <= numero:
    if numero % i == 0:
        divisores = divisores + 1
    i = i + 1

if divisores == 2:
    print(numero, "es primo")
else:
    print(numero, "no es primo")