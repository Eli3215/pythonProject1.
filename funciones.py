# Importación de modulos
from os import system
from Producto import Factory, Producto

# Esta función permite limpiar la consola
# Parámetros de entrada: Ninguno
# Retorna: No
def limpiar_consola() -> None:
    system('cls')


# Función para crear productos
# Parámetros de ingreso: Se ingresa el tipo, nombre, precio y cantidad del producto
# Retorna: producto creado
def ingresar_producto( tipo_producto, nombre_producto, precio_producto, cantidad_producto ) -> Producto:

    # Llamado a la clase factory
    factory = Factory()


    # Creación de un producto (Fruta o Verdura) dependiendo del tipo de producto requerido
    # usando la clase Factory
    producto = factory.crear_producto( tipo_producto )

    # Se establecen las caracteristicas del producto excepto el codigo, ya que este se actualiza de manera automática
    producto.establecer_codigo_producto()
    producto.establecer_nombre_producto( nombre_producto )
    producto.establecer_precio_producto( precio_producto )
    producto.establecer_cantidad_producto( cantidad_producto )
    return producto


# Función que permite imprimir el inventario en forma de tabla
# Parámetros de ingreso: la instancia del inventario
# Retorna: el mensaje a ser impreso en la consola
def imprimir_inventario( inventario ) -> str:
    mensaje = inventario.imprimir_inventario()
    mensaje += inventario.actualizar_productos_disponibles_en_estanteria()
    return mensaje

# Función que permite actualizar la factura de venta
# Parámetros de ingreso: la instancia del inventario y el código del producto a buscar en el inventario
# Retorna: el precio actual de la factura a ser impreso en la consola
def retornar_precio_producto( inventario, codigo_producto ) -> float:

    precio = 0.0

    # Se busca en el inventario los productos que empiecen por f para las frutas o por v para las verduras para retornar
    # el precio del producto. Si no se ingresa un código correcto, se imprime un mensaje de que no se encontró
    # el producto y se retorna el valor 0.0
    if codigo_producto.find("f") != -1:
        producto = inventario.retornar_Fruta(codigo_producto)
        precio = producto.retornar_precio_producto()
    elif codigo_producto.find("v") != -1:
        producto = inventario.retornar_Verdura(codigo_producto)
        precio = producto.retornar_precio_producto()
    else:
        print("No se encotró el producto")

    return precio
