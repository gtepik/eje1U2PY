class CuentaBancaria:
    def __init__(self, saldo):  
        self.saldo = saldo
        
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Has depositado {cantidad} en tu cuenta.")  
        
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes suficiente saldo en tu cuenta.")
        else:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad} de tu cuenta.")  
            
    def consultar_saldo(self):  
        print(f"Tu saldo es {self.saldo}")
saldo_inicial = float(input("Ingrese el saldo inicial: "))
cuenta = CuentaBancaria(saldo_inicial)
cantidad = float(input("¿Cuánto quieres depositar? "))
cuenta.depositar(cantidad)
cuenta.consultar_saldo()
cantidad = float(input("¿Cuánto quieres retirar? "))
cuenta.retirar(cantidad)
cuenta.consultar_saldo()
