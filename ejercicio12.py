#Dado un número entero, crea un algoritmo que determine si es primo o no

def ejercicio12():
    numero = int(input("Introduzca un numero: "))
    esPrimo = True

    if numero < 2:
        esPrimo = False

    for i in range(2,numero,1):
        if numero % i == 0:
            esPrimo = False
            break

    if esPrimo:
        print(numero, "es primo")
    else:
        print(numero, "no es primo")