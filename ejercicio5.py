def ejercicio5():
    try:
        n = int(input("Introduzca el número de enteros de la lista: "))
        listaEnteros = []
        for i in range(n):
            listaEnteros.append(int(input(f"Introduzca el entero de la posición {i}: ")))
    except Exception as e:
            print(f"Se ha producido el error: \n{e} \nPorque el número introducido es inválido")
    else: 
        print("La lista que ha introducido es:", listaEnteros)
        listaOrdenada = sorted(listaEnteros)
        menorNumero = listaOrdenada[0]
        mayorNumero = listaOrdenada[-1]
        print(f"El menor y el mayor elemento de la lista introducida son {menorNumero} y {mayorNumero}, respectivamente")