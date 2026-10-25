presentes = 0
ausentes = 0

letra = input("Ingrese P (presente), A (ausente) o F (fin): ").upper()

while letra != "F":
    if letra == "P":
        presentes = presentes + 1
    elif letra == "A":
        ausentes = ausentes + 1
    else:
        print("Letra no valida")
    letra = input("Ingrese P (presente), A (ausente) o F (fin): ").upper()

print("Presentes:", presentes)
print("Ausentes:", ausentes)