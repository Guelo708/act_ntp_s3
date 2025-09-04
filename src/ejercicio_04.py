suma = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
print("Suma total:", suma)