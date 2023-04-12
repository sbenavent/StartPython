#Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.

def ejercicio13():
    try:
        aristaCubo = float(input("Introduzca la arista del cubo: "))
    
    except ValueError:
         print("Se ha producido un error.Debe introducir un numero entero")

    else:

        areaCubo = (aristaCubo * aristaCubo) * 6
        volumenCubo = aristaCubo ** 3

        print("El area del cubo es: ", areaCubo)
        print("El perimetro del cubo es: ", volumenCubo)