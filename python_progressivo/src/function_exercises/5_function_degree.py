def to_celsius(temperature):
    celsius = (temperature - 32)/1.8
    print("Fahrenheit:", temperature, " to Celsius:", celsius)


def to_fahrenheit(temperature):
    fahrenheit = 1.8 * temperature + 32
    print("Celsius:", temperature, " to Fahrenheit:", fahrenheit)


while True:
    option = int(input("Insert option: 1 - Celsius/ 2 - Fahrenheit"))
    if option == 1:
        temperature = float(input("Insert temperature:"))
        to_celsius(temperature)
    elif option == 2:
        temperature = float(input("Insert temperature:"))
        to_fahrenheit(temperature)
    else:
        print("Opção inválida.")
        break
