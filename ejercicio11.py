#Crea un algoritmo que calcule el factorial de un número entero
def ejercicio11():
    numero = int(input("Introduzca un numero: "))
    factorial = 1
    for i in range(1, numero+1,1):
        factorial *= i

    print("El factorial de ", numero, " es ", factorial)
