def ejercicio7():
    try:
        numero = int(input("Introduzca un número entero: "))
    except Exception as e:
            print(f"Se ha producido el error: \n{e} \nPorque el número introducido es inválido")
    else:
        if numero%2 == 0:
            print(f"El número introducido, es decir el {numero}, es par")
        else:
            print(f"El número introducido, es decir el {numero}, es impar")