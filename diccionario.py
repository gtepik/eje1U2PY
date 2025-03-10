def eliminar(listas):
    lista = []
    for elemento in listas:
        if elemento not in lista:
            lista.append(elemento)
    return lista

def frecuencia(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.strip(".,!?()[]{}:;'")
        if palabra:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def invertir(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        if valor in invertido:
            if type(invertido[valor])== list:
                invertido[valor].append(clave)
            else:
                invertido[valor] = [invertido[valor], clave]
        else:
            invertido[valor] = clave
    return invertido
listas = [1,2,2,3,4,4,5,6,6,6,6,7]
print("nmero sin duplicar:", eliminar(listas))

texto = "BIENVENIDO gt , bienvenido  epik como esta llendo  tu dia, esta muy bien por hoy hare un program en gt epik "
print(frecuencia(texto))


diccionario = {"a": 1, "b": 2, "c": 1, "d": 3}
print("nmeros invertidos:", invertir(diccionario))
