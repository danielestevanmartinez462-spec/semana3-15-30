saldo = 500000
retiro = 1

while retiro != 0 and saldo > 0:
    print("Saldo:", saldo)
    retiro = int(input("Cuanto quiere retirar (0 para salir): "))
    if retiro > saldo:
        print("No tiene saldo suficiente")
    else:
        saldo = saldo - retiro

print("Saldo restante:", saldo)