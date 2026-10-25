import time

segundos = 1

while segundos <= 5:
    print(segundos)
    time.sleep(1)
    segundos = segundos + 1

print("Tiempo de espera agotado (Timeout)")