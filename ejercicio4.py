from math import pi
def areaPerimetro(radio):
    area = round(radio*pi*2,4)
    perimetro = round(pow(radio,2)*pi,4) 
    return area, perimetro
def ejercicio4():
    try:
        numero = float(input("Introduzca el radio del círculo: "))
    except Exception as e:
        print(f"Se ha producido el error: \n{e} \nPorque el número introducido es inválido")
    else: 
        area , perimetro = areaPerimetro(numero)
        print(f"El área del círculo es {area} y el perímetro del círculo es {perimetro}")
if __name__ == "__main__":
    ejercicio4()