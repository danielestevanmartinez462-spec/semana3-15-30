numero = int(input("Ingrese un numero entero: "))
suma = 0

while numero > 0:
    digito = numero % 10
    suma = suma + digito
    numero = numero // 10

print("La suma de los digitos es:", suma)