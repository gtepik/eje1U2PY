"""class Pelicula:
    def __init__(self, titulo, year, descripcion, director, calificacion):
        print("Creando una nueva película...")
        self.titulo, self.year, self.descripcion, self.director, self.calificacion = titulo, year, descripcion, director, calificacion

    def imprimir_info(self):
        print(f"Mostrando información de la película: {self.titulo}")
        print(f"Título: {self.titulo}\nAño: {self.year}\nDescripción: {self.descripcion}\nDirector: {self.director}\nCalificación: {self.calificacion}/10\n" + "-" * 40)

peliculas = [
    Pelicula("Marvel", 2010, "Superhéroes salvan el mundo.", "Christopher Nolan", 9.0),
    Pelicula("The Matrix", 1999, "Un hacker descubre la verdad.", "Lana y Lilly Wachowski", 8.7),
    Pelicula("Interstellar", 2014, "Exploración espacial.", "Christopher Nolan", 8.6),
    Pelicula("Titanes del Pacífico", 2013, "Robots contra bestias.", "Guillermo del Toro", 9.2),
    Pelicula("One Piece", 1997, "Un chico quiere ser rey pirata.", "Eiichiro Oda", 8.6)
]

def agregar_pelicula():
    print("Agregando una nueva película...")
    titulo = input("Título: ")
    year = input("Año: ")
    descripcion = input("Descripción: ")
    director = input("Director: ")
    try:
        calificacion = float(input("Calificación (0-10): "))
        if 0 <= calificacion <= 10:
            peliculas.append(Pelicula(titulo, int(year), descripcion, director, calificacion))
            print("Película agregada exitosamente.")
        else:
            print("Calificación inválida.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_pelicula():
    print("Eliminando una película...")
    for i in range(len(peliculas)):
        print(f"{i + 1}. {peliculas[i].titulo}")
    try:
        opcion = int(input("Seleccione el número de la película a eliminar: "))
        if 1 <= opcion <= len(peliculas):
            print(f"Eliminando la película: {peliculas[opcion - 1].titulo}")
            peliculas.pop(opcion - 1)
            print("Película eliminada exitosamente.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\nMenú de Películas")
        for i in range(len(peliculas)):
            print(f"{i + 1}. {peliculas[i].titulo}")
        print("6. Agregar Película")
        print("7. Eliminar Película")
        print("8. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 8:
                if opcion == 8:
                    print("Saliendo del programa...")
                    break
                elif opcion == 6:
                    agregar_pelicula()
                elif opcion == 7:
                    eliminar_pelicula()
                else:
                    pelicula = peliculas[opcion - 1]
                    pelicula.imprimir_info()
                    if input("¿Editar calificación? (s/n): ").lower() == 's':
                        try:
                            nueva_calificacion = float(input("Nueva calificación (0-10): "))
                            if 0 <= nueva_calificacion <= 10:
                                pelicula.calificacion = nueva_calificacion
                                print("Calificación actualizada a", pelicula.calificacion)
                            else:
                                print("Valor inválido.")
                        except ValueError:
                            print("Entrada inválida.")
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida.")

print("Iniciando el programa...")
menu()
print("Programa finalizado.")"""
