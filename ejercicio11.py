#Crea un algoritmo que calcule el factorial de un número entero
def ejercicio11():
    try:
        numero = int(input("Introduzca un numero: "))

    except ValueError:
        print("Se ha producido un error.Debe introducir un numero entero")

    else:

        factorial = 1
        for i in range(1, numero+1,1):
            factorial *= i

        print("El factorial de ", numero, " es ", factorial)
