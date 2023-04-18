def ejercicio6():
    try:
        gradosCelsius = float(input("Introduzca la temperatura en grados Celsius: "))
    except Exception as e:
        print(f"Se ha producido el error: \n{e} \nPorque la temperatura introducida es inválido")
    else:
        gradosFahrenheit = round(gradosCelsius*1.8 + 32,4)
        print(f"{gradosCelsius} grados Celsius son {gradosFahrenheit} grados Fahrenheit")
if __name__ == "__main__":
    ejercicio6()
