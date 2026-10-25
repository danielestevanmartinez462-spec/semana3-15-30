numero = int(input("Ingrese un numero (0 para terminar): "))
maximo = numero

while numero != 0:
    if numero > maximo:
        maximo = numero
    numero = int(input("Ingrese un numero (0 para terminar): "))

print("El numero mas alto fue:", maximo)