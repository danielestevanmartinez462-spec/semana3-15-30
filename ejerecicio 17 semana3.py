total = 0
precio = int(input("Precio del producto: "))

while precio != 0:
    total = total + precio
    precio = int(input("Precio del producto: "))

print("Total a pagar:", total)