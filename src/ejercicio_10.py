# Lee palabras hasta que el usuario escriba "fin"
contador = 0
while True:
    palabra = input("Escribe una palabra ('fin' para terminar): ")
    if palabra.lower() == "fin":
        break
    contador += 1
print("Cantidad de palabras ingresadas:", contador)