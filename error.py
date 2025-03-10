"""from errorpersonalizado import ErrorPersonalizado

try:
 numero1 = int(input("ingresa el primer nuemro"))
 numero2 = int(input("ingresa el segundo nuemro"))
 if numero1 == numero2:
     raise ErrorPersonalizado("los nuemros ingresados son identicos ")
 else:
     suma = numero1 + numero2
     print(f"la suma de los numeros es {suma}")
except Exception as e:
    print(f"se ha agregado un error:{e}")
else:
    print(f"no se ha generado un error")
finally:
    print("se ha terminado la ejecucion")
    """
    
    
    
    
    



#generear un programa que te permita ingresar una lista de 10 numeros al final del programa debera devolver la lista en orden de menor a mayor debe genrar un error si ingresar un nuemro negativo un decimal o repetido 
# Función para solicitar 10 números enteros positivos al usuario

def obtener():
    while True:
        try:
            entrada = input("ingresa 10 nmeros  separados por espacios: ")
            numeros = [int(x) for x in entrada.split()]
            if len(numeros) != 10:
                print("solo 10 umeros ")
                continue
            if len(numeros) != len(set(numeros)):
                print("no se permiten numer repetidos")
                continue
            if any(num < 0 for num in numeros):
                print("no se permiten nmeros negativos")
                continue
            return numeros
        except ValueError:
            print("ingresar solo nmeros  enteros")

def main():
    numeros = obtener()
    numeros.sort()
    print("Lista ordenada:", numeros)

if __name__ == "__main__":
    main()




  
    