from time import sleep
from os import system
from Producto import Factory

# Esta función permite limpiar la consola
# Parámetros de entrada: Ninguno
# Retorna: No
def limpiar_consola() -> None:
    system('cls')

# Esta función permite mostrar el menú al administrador de la caja registradora
# Parámetros de entrada: Ninguno
# Retorna: La opción para continuar con las opciones en caja
def mostrar_menu_administrador() -> str:
    print('Hola administrador, seleccione la acción que desea realizar:')
    print('1. Ingresar productos al inventario')
    print('2. Realizar una venta a un cliente')
    print('3. Salir')
    print('****************************************')

    opcion = int(input('Ingrese la opción a realizar -> '))
    return opcion

def computar_producto( ) -> None:

    # La variable alimento permite definir la categoria del alimento que se va a procesar en el sistema
    limpiar_consola()
    alimento = int(input('Ingrese el producto a pagar -> '))

    if alimento == 1:
        factory = Factory()
        producto = factory.crear_producto('Fruta')

        producto.establecer_nombre_producto( 'banano' )
        producto.establecer_precio_producto( 1400 )
        print(producto.venta_producto())
    elif alimento == 2:

        factory = Factory()
        producto = factory.crear_producto('Verdura')

        producto.establecer_nombre_producto( 'tomate' )
        producto.establecer_precio_producto( 2500 )
        print(producto.venta_producto())
    else:
        print('Error de sistema')