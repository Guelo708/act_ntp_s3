# Suma de los dígitos de un número ingresado
numero = input("Ingrese un número entero positivo: ")
suma = 0
for digito in numero:
    suma += int(digito)
print("Suma de los dígitos:", suma)