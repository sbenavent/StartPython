#Menú principal
import os
from ejercicio1 import ejercicio1
from ejercicio2 import ejercicio2
from ejercicio4 import ejercicio4
from ejercicio5 import ejercicio5
from ejercicio6 import ejercicio6
from ejercicio7 import ejercicio7
from ejercicio8 import ejercicio8
from ejercicio9 import ejercicio9
from ejercicio10 import ejercicio10
from ejercicio11 import ejercicio11
from ejercicio12 import ejercicio12
from ejercicio13 import ejercicio13
from ejercicio14 import ejercicio14
from ejercicio15 import ejercicio15
from ejercicio16 import ejercicio16
from ejercicio17 import ejercicio17
from ejercicio18 import ejercicio18
from ejercicio19 import ejercicio19
from ejercicio20 import ejercicio20

while True:
    os.system("cls") #Limpia la pantalla cada vez que se vuelve al menú
    print("Bienvenido/a al Menú principal. Este programa recoge todos los ejercicios de Algoritmos. Seleccione el algoritmo que desea usar de la lista.")
    print("1 - Cálculo de letra DNI.")
    print("2 - Cálculo del salario")
    print("4 - Área y perímetro de un círculo")
    print("5 - Ordenación de números enteros.")
    print("6 - Conversor de Farenheit a Celsius")
    print("7 - Determinar si un número es par o impar")
    print("8 - Determinar si un año es bisiesto")
    print("9 - Saber si un texto es un palíndromo")
    print("10 - Ordenar alfabéticamente")
    print("11 - Cálculo de factoriales.")
    print("12 - Saber si un número es primo")
    print("13 - Volumen de un cubo")
    print("14 - Suma de números pares")
    print("15 - Saber si un número es positivo, negativo o 0.")
    print("16 - Cálculo de medias")
    print("17 - Juego de número aleatorio")
    print("18 - Saber si dos textos son anagramas.")
    print("19 - Eliminar números duplicados")
    print("20 - Determinar si un número es capicúa")
    
    print("Introduzca el número del algoritmo que quiere usar o introduzca 0 para cerrar el programa")
    opcion = int(input())

    if opcion == 0: 
        input("Gracias por usar el programa. Pulse ENTER para salir.")
        break
    elif opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 4:
        ejercicio4()
    
