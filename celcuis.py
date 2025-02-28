CELSIUS_TO_FAHRENHEIT = lambda c: (c * 9/5) + 32  
FAHRENHEIT_TO_CELSIUS = lambda f: (f - 32) * 5/9  
CELSIUS_TO_KELVIN = lambda c: c + 273.15
KELVIN_TO_CELSIUS = lambda k: k - 273.15

def convertir_temperatura():
    while True:
        print("\nMenú de Conversión de Temperaturas:")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Celsius a Kelvin")
        print("4. Kelvin a Celsius")
        print("5. Salir")        
        opcion = input("Seleccione una opción: ")     
        if opcion == "1":
            c = float(input("Ingrese la temperatura en Celsius: "))
            print(f"{c}°C = {CELSIUS_TO_FAHRENHEIT(c):.2f}°F")
        elif opcion == "2":
            f = float(input("Ingrese la temperatura en Fahrenheit: "))
            print(f"{f}°F = {FAHRENHEIT_TO_CELSIUS(f):.2f}°C")
        elif opcion == "3":
            c = float(input("Ingrese la temperatura en Celsius: "))
            print(f"{c}°C = {CELSIUS_TO_KELVIN(c):.2f}K")
        elif opcion == "4":
            k = float(input("Ingrese la temperatura en Kelvin: "))
            print(f"{k}K = {KELVIN_TO_CELSIUS(k):.2f}°C")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
if __name__ == "__main__":
    convertir_temperatura()