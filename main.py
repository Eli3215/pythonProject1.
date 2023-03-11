# Importación de módulos
from funciones import limpiar_consola, ingresar_producto, imprimir_inventario, actualizar_factura_venta
from SingletonInventario import Inventario
from Venta import Venta

# Inicio del programa
if __name__ == "__main__":

    # Inicialización de variables
    inventario = Inventario()
    inventario.inicializacion()
    venta = Venta()

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

        # Ingresar productos al inventario
        if opcion == 1:

            limpiar_consola()

            print('Para ingresar Fruta escriba 1, o para ingresar Verdura escriba 2')

            tipo_producto = int(input('Ingrese la opción a realizar -> '))

            nombre_producto = str(input('Ingrese el nombre del producto -> '))

            precio_producto = int(input('Ingrese el precio unitario del producto -> '))

            cantidad_producto = int(input('Ingrese la cantidad del producto -> '))

            if tipo_producto == 1:
                producto = ingresar_producto('Fruta', nombre_producto, precio_producto, cantidad_producto)
                inventario.agregar_fruta(producto)
                print('Producto agregado')

            elif tipo_producto == 2:
                producto = ingresar_producto('Verdura', nombre_producto, precio_producto, cantidad_producto)
                inventario.agregar_verdura(producto)
                print('Producto agregado')

            else:
                print('Ingreso equivocado, intente de nuevo')



        # Ver el inventario de productos
        elif opcion == 2:
            limpiar_consola()

            imprimir_inventario(inventario)
            input('Ingrese Enter para continuar')

        # Realizar una venta a un cliente
        elif opcion == 3:

            codigo_producto = ""

            # Se llama este método de la clase para reiniciar los valores de la factura de venta
            venta.preparar_nueva_venta()

            while codigo_producto != "xx":
                limpiar_consola()
                imprimir_inventario(inventario)
                codigo_producto = input(
                    'Ingrese el código de venta del producto que desea comprar, o xx para proceder a pagar -> ')

                # Se llama esta función para buscar el producto en el inventario y retornar el costo del producto
                precio_producto = actualizar_factura_venta(inventario, codigo_producto)

                # Se llama al método acumular venta para ir agregando el costo a la factura
                venta.acumular_venta(precio_producto)

                limpiar_consola()
                print("==================================================")
                print(f'Valor factura: {venta.retorna_valor_venta()}')
                print("==================================================\n")
                input('Ingrese Enter para continuar')

        # Salir del sistema
        elif opcion == 0:
            limpiar_consola()
            print('Fin de la jornada en la tienda!!!!')
            break

        # Error de ingreso
        else:
            print('Opción incorrecta, intente de nuevo!!!')
