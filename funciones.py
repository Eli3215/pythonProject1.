from time import sleep
from os import system
from Producto import Factory, Producto

# Esta función permite limpiar la consola
# Parámetros de entrada: Ninguno
# Retorna: No
def limpiar_consola() -> None:
    system('cls')

# Función para crear productos
# Parámetros de ingreso: Se ingresa el tipo, nombre y precio del producto
# Retorna: producto creado
def ingresar_producto( tipo_producto, nombre_producto, precio_producto ) -> Producto:
    factory = Factory()
    producto = factory.crear_producto( tipo_producto )
    producto.establecer_nombre_producto( nombre_producto )
    producto.establecer_precio_producto( precio_producto )
    return producto