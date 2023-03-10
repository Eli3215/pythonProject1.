# Importación de módulos
from funciones import limpiar_consola, ingresar_producto
from time import sleep
from SingletonInventario import Inventario

# Inicio del programa
if __name__ == "__main__":

    # Inicialización de variables
    inventario = Inventario()
    inventario.inicializacion()

    # Este ciclo infinito permitirá consultar permanentemente las opciones del menú
    # en la caja registradora
    while True:

        limpiar_consola()

        # Impresión del menú inicial
        print('Hola administrador, seleccione la acción que desea realizar:')
        print('1. Ingresar productos al inventario')
        print('2. Ver el inventario de productos')
        print('3. Realizar una venta a un cliente')
        print('0. Salir')
        print('****************************************')

        opcion = int(input('Ingrese la opción a realizar -> '))

        if opcion == 1:
            limpiar_consola()
            print('Para ingresar Fruta escriba 1, o para ingresar Verdura escriba 2')
            tipo_producto = int(input('Ingrese la opción a realizar -> '))

            nombre_producto = str(input('Ingrese el nombre del producto -> '))

            precio_producto = int(input('Ingrese el precio unitario del producto -> '))

            if tipo_producto == 1:
                producto = ingresar_producto('Fruta', nombre_producto, precio_producto)
                inventario.agregar_fruta(producto)
                print('Producto agregado')
            elif tipo_producto == 2:
                producto = ingresar_producto('Verdura', nombre_producto, precio_producto)
                inventario.agregar_verdura(producto)
                print('Producto agregado')
            else:
                print('Ingreso equivocado, intente de nuevo')

        elif opcion == 2:
            limpiar_consola()
            inventario.imprimir_inventario()
            sleep(5)  # Se espera unos segundos para actualizar la consola

        elif opcion == 3:
            print('Falta implementar la venta')

        elif opcion == 0:
            limpiar_consola()
            print('Fin de la jornada en la tienda!!!!')
            break

        else:
            print('Opción incorrecta, intente de nuevo!!!')

        sleep(3)  # Se espera unos segundos para actualizar la consola
