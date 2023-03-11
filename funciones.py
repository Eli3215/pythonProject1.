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
def ingresar_producto( tipo_producto, nombre_producto, precio_producto, cantidad_producto ) -> Producto:

    factory = Factory()

    producto = factory.crear_producto( tipo_producto )
    producto.establecer_codigo_producto()
    producto.establecer_nombre_producto( nombre_producto )
    producto.establecer_precio_producto( precio_producto )
    producto.establecer_cantidad_producto( cantidad_producto )
    return producto


# Función permite imprimir el inventario en forma de tabla
# Parámetros de ingreso: la instancia del inventario
# Retorna: No
def imprimir_inventario( inventario ) -> None:
    mensaje = inventario.imprimir_inventario()
    mensaje += inventario.actualizar_productos_disponibles_en_estanteria()
    print(mensaje)


def actualizar_factura_venta( inventario, codigo_producto ) -> float:

    precio = 0.0
    if codigo_producto.find("f") != -1:
        producto = inventario.retornar_Fruta(codigo_producto)
        precio = producto.retornar_precio_producto()
    elif codigo_producto.find("v") != -1:
        producto = inventario.retornar_Verdura(codigo_producto)
        precio = producto.retornar_precio_producto()
    else:
        print("No se encotró el producto")

    return precio
