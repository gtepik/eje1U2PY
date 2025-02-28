class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustible = 100  # Inicia con 100 litros

    def conducir(self, km):
        consumo = km / 10  # 1 litro cada 10 km
        if self.combustible >= consumo:
            self.combustible -= consumo
            print(f"Has conducido {km} km. Combustible restante: {self.combustible:.1f} litros.")
        else:
            print("No hay suficiente combustible para recorrer esa distancia.")
    
    def repostar(self, litros):
        if litros <= 0:
            print("Cantidad de litros inválida.")
            return
        
        if self.combustible + litros > 100:
            litros = 100 - self.combustible
        
        self.combustible += litros
        print(f"Has repostado {litros} litros. Combustible actual: {self.combustible:.1f} litros.")
    
    def estado(self):
        print(f"Combustible restante: {self.combustible:.1f} litros.")

# Ejemplo de uso
coche = Coche("Toyota", "Corolla")
coche.estado()
km_a_recorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
coche.conducir(km_a_recorrer)
coche.estado()
litros_a_repostar = int(input("¿Cuántos litros quieres repostar? "))
coche.repostar(litros_a_repostar)
coche.estado()
