
'''cadena:str ="cadena"
#cadena = 1
booleano :bool = True 
decimal  :float= 10.6
#cadena = 100
#, para unir en el print
#print("el valor de la cadena es " + cadena)
#print("el valor de la cadena es " , decimal)
#print(f"el del entero es :{entero}")
print(f"el valor de la cadena {cadena} y es de tipo {type(cadena)}".center(80,"*"))
print(f"el valor de la booleano {booleano} y es de tipo {type(booleano)}".center(80,"*"))
print(f"el valor de la float {decimal} y es de tipo {type(decimal)}".center(80,"*"))
#print(type(decimal))
print(type(cadena))
#el id dereccion de memoria ver la direccion de memoria de una variable 
print(id(cadena))
#euqivalemte a un escaner
#input todo lo que reciba se va a hacer un cadena 
nombre  = input("ingresa tu nombre: ")'''
#print(type(nombre) ,id(nombre))
#print("hola mundo , "+ nombre)
#nombre = "laura "
#print(type(nombre) ,id(nombre))
#print("hola mundo , "+ nombre)

#estructura de control 
""" nombre = input("ingresa tu nombre:")
print("antes del if")
if  nombre == "epik":
    print("el nombre es" + nombre)
elif nombre == "laura":
    print("el nombre no es igual" + nombre)
else:
    print("el nombre no es igual  a epik")
print("fin del programma ")    """ 
   
   
   
   
""" nombre1 = input("ingresa tu nombre:")
print("antes del if")
print(type(nombre1))
if  nombre1 == "epik":
    print("el nombre es" + nombre1)
elif nombre1 == "laura":
    print("el nombre no es igual" + nombre1)
else:
    print("el nombre no es igual  a epik")
print("fin del programma ")  """

#que determini si un nuemro es par o inpar     
    
'''numero = int(input("ingresa un nuemro:"))
print("antes del if ")
if numero % 2 == 0:
    print("el nuemro es par")
else:
    print("el nuermo es impar") 
print("find del programa ")     '''  


'''
cadena:str = input("ingresa tu nombre")      
contador :int=0
for i in cadena:
    print(i ,end="-")
    contador +=1
print(f'\nEL nombre tiene {contador}letreas')'''

#arreglo
'''lista=[1,2,3,4,5]
print(lista)
print(type(lista))
lista.append(6)
lista.insert(1,10)#replaza el lugar del 2 por el 10
print(lista)
lista.remove(1)#eliminar el 1 por el 10
print(lista)
lista.pop()#remueve el ultimo valor
print(lista)
del lista[2]#elimina la posicion 2
print(lista)
lista.clear()#limpia todo pero  no elimina 
print(lista)
del lista
print(lista) '''

'''tupla = ('epik','cesar','fer')
print(type(tupla))#impresion de la tupla
print(tupla)#permmite contar cuantas veces existen un valor em la tupla 
print(tupla.count('diego'))#sirve para contar cuantas veces se repite 
print(tupla.index('epik'))#permite saber en que posicion se encentara un valor en especifica y si hat dos solo pone el primero 
print(tupla[2])
lista_tupla=list()
for i in tupla:#recorremos la tupla y llenamos el lugar 
    lista_tupla.append(i)
print(type(lista_tupla))#impresion de tipo de dato
print(lista_tupla)
lista_tupla[3]="mario"#modifica la posicion 3 de la lista
print(lista_tupla)#convertimso la lsita en una tupla 
lista_tupla = tuple(lista_tupla)#impresion de tipo de dato
print(type(lista_tupla))
print(lista_tupla)'''


'''#colecciones set 

coleccion = {'pizza','tacos','tamales','milanesa','amburgesa'}
print(type(coleccion))
print(coleccion)
coleccion.add('tortas')
print(coleccion)
coleccion.add('tacos')# agrega 
print(coleccion)
coleccion.clear() #limpia 
print(coleccion)
coleccion.discard('tortas')#elimar un elemento dentro de una coleccion 
print(coleccion)
del coleccion    #elimina la coleccion
print(coleccion)'''
#progrma q permita ingresar n numero nombres sin validacion 

    
    
'''n = int(input("¿Cuántos nombres deseas ingresar? "))#n numero entero , int cadena a nuemro , input captura los datos 
nombres = [input(f"Ingresa el nombre {i+1}: ") for i in range(n)]#recorre desde 0 hasta n numeros crea umas cadena 

print("\nLos nombres ingresados son:")#con el for se imprme los nombres  y el pint los imprime 
for nombre in nombres:
    print(nombre)
    
#lo hiso diego 
n = int(input("ingresa la cantidad de datos:"))
nombres  = list()
for i in range(n):
    nombre.append(input(f"({i+1})ingresar el nombre:"))
print(nombres)'''

#diccionario 
'''diccionario={"nombre":"epik","carrera":"sistemas","semestre":10}
print(type(diccionario))
print('carrera' in diccionario)# in permitre saber si existe una llave en diccionario 
print(diccionario['carrera'])#imprime el valor de la llave 
print(diccionario.get('nombre'))#para accedera a la misma llave 
for i in diccionario.items():#con items imprime los datos como si fuera una tupla 
    print(i)
for i in diccionario.keys():#muestra solo las llaves ingresadas
    print(i)
for i in diccionario.values():#muestra solo los valores ingresados 
    print(i)
for i,j in diccionario.items():# i se casa con el valor y j con el valor 
    print(i,j)
    
diccionario['especialidad']= "aplicaciones web"#agrega una llavve nueva
print(diccionario)

diccionario.pop("semestre")#elimina la llave semstre
print(diccionario)
'''


#funciones 
'''def funcion(nombre = "sin nombre") -> str :    #indicar el tipo de dato 
    print(f"hola mundo {nombre}")
funcion()'''

'''def funcion(nombre = "sin nombre") -> str :    #indicar el tipo de dato 
    return nombre
    print(f"hola mundo {funcion (epik)}")'''
'''
def funcion(*nombre) -> str :    # * recibira n numeros de datos  
    return nombre
print(f"hola mundo {funcion("epik","cesar","fer","ana")}")


def funcion(grupo,semestre,*nombre) -> str :    #indicar el tipo de dato 
    print(grupo)
    print(semestre)
    print(nombre)
    return "impresion"
print(f"hola mundo {funcion("sistemas",8,"epik","cesar","fer","ana")}")'''

#programa dividir en funciones matrai grupo carrera horario lista alumnos 
"""
def datos1():
    nombre1 = input("Ingresa tu primer nombre: ")
    nombre2 = input("Ingresa tu segundo nombre: ")
    materia = input("Ingresa la materia: ")
    grupo = input("Ingresa el grupo: ")
    carrera = input("Ingresa la carrera: ")
    horario = input("Ingresa el horario: ")
    numCo = input("Ingresa el número de control: ")
    return [(nombre1, nombre2, materia, grupo, carrera, horario, numCo)]

def datos2(nombres) -> str:
    for nombre1, nombre2, materia, grupo, carrera, horario, numCo in nombres:
        print(f"\nPrimer Nombre: {nombre1}")
        print(f"Segundo Nombre: {nombre2}")
        print(f"Materia: {materia}")
        print(f"Grupo: {grupo}")
        print(f"Carrera: {carrera}")
        print(f"Horario: {horario}")
        print(f"Número de Control: {numCo}")
    return "personal"

nombres = datos1()
print(f"\nEsta es tu información: {datos2(nombres)}")"""


def parametro_multiple(**parametro):
    print(parametro)

parametro_multiple(titulo = "test" , numero=2, booleano = True , decimal = 10.10)
"""kworks"""""


def parametro_multiple(nombre = "" , apellido ="" ,edad=0):
    print(nombre,apellido,edad)
    
parametro_multiple(apellido="alv",)


"u2"
