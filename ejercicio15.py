#Crea un algoritmo que determine si un número es positivo, negativo o cero.

def ejercicio15():

    try:
        numero = int(input("Introduzca un numero: "))

    except ValueError:
         print("Se ha producido un error.Debe introducir un numero entero")
    
    else:

        if numero < 0:
            print(numero, "es negativo")
        elif numero == 0:
            print(numero, "es 0")
        else:
            print(numero, "es positivo")