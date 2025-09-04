# Juego de adivinanza
import random

numero_secreto = random.randint(1, 10)
intento = None

while intento != numero_secreto:
    intento = int(input("Adivina el número (1 al 10): "))
    if intento != numero_secreto:
        print("Incorrecto. Intenta otra vez.")
print("¡Felicidades! Adivinaste el número.")