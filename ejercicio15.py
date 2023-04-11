#Crea un algoritmo que determine si un número es positivo, negativo o cero.

def ejercicio15():
    numero = int(input("Introduzca un numero: "))

    if numero < 0:
        print(numero, "es negativo")
    elif numero == 0:
        print(numero, "es 0")
    else:
        print(numero, "es positivo")