deuda = float(input("Valor de la deuda: "))
meses = int(input("Meses en mora: "))

contador = 0
while contador < meses:
    deuda = deuda + deuda * 0.05
    contador = contador + 1

print("Saldo final:", deuda)