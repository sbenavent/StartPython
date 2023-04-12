#Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.

def ejercicio14():
  
    numeros = [2, 5, 17, 32, 51, 68, 74, 86]
    sumaPares = 0

    for i in range (0, len(numeros),1):
            if numeros[i] % 2 == 0:
                sumaPares += numeros[i]

    print("La suma total de los numeros pares es: ", sumaPares)


