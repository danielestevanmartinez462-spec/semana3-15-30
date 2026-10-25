stock = 20

while stock > 0:
    print("Stock:", stock)
    venta = int(input("Cuantas unidades vende: "))
    if venta > stock:
        print("Error, no hay suficiente stock")
    else:
        stock = stock - venta

print("Se acabo el stock")