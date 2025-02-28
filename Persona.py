from mis_constantes import NOMBRE ,CARRERA

class Persona:     #doble yon bajo es que le pertenece a una  clase
    
    CONSTANTE = "TEST"
    test = "prueba"
    def __init__(self, nombre, apellido, edad, sexo):  # el def es equivalente a this 
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sexo = sexo
        # constructor
    @property #hace 
    def nombre(self):
        return self._nombre
    @property 
    def apellido(self):
        return self._apellido
    @property 
    def edad(self):
        return self._edad
    @property  
    def sexo(self):
        return self._sexo
    
    @nombre.setter  
    def nombre(self,nombre):
        self._nombre = nombre  
    @apellido.setter  
    def apellido(self,apellido):
        self._apellido = apellido
    @edad.setter
    def edad(self,edad):
        self._edad = edad
    @sexo.setter 
    def sexo(self,sexo):
        self._sexo = sexo    
    
    @staticmethod
    def mostrar_variables():
        print(Persona.test)
    
    @classmethod
    def leer_contenido(cls): #cls referncia a metodo de clase 
        print(cls.nombre)
        
    def mostrar(self):
        print(f"Datos: Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}, Sexo: {self._sexo}")

persona1 = Persona("epik", "alv", 20, "m")
print(persona1.nombre)
persona1.nombre="epik"
persona1.mostrar()
persona1.apellido="alv"
persona1.mostrar()
persona1.edad=20
persona1.mostrar()
persona1.sexo="M"
persona1.mostrar()
Persona.mostrar_variables() #es de acceso rapido 

persona1
'''print(type(persona1))
persona1.mostrar()
print(__name__)
print(persona1.nombre())'''



CRAR UN ARCHIVO DE CONSTATNTE  UNA FORMLA DE FARENGEIT  A CELCIUS 
DE CELCIUAS A FARANGEIT
 CELCIUAS A KELVIN 
 Y DE KELVIN A CELCIUS
 A UNA CLESE U DENTO UN METODO 
MENU QUE PIDOA A QUE CONVERTIR 
