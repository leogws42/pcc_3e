# cuando se crea una variable tiene que ser en minuscula
class MenuItem():
        def __init__(self, inventario, nombre, precio):
            self.inventario = inventario
            self.nombre = nombre
            self.precio = precio

        def venta(self):
              self.inventario = self.inventario -1

bandeja_paisa = MenuItem(20,"bandeja paisa",13_500)
print(f"me quedan a esta hora del dia {bandeja_paisa.inventario} bandejas paisas")
bandeja_paisa.venta()
print(f"me quedan a esta hora del dia {bandeja_paisa.inventario} bandejas paisas")

# print(f"me quedan a esta hora del dia {bandeja_paisa.inventario} bandejas paisas")
    
