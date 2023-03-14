# Importación de módulos
from funciones import limpiar_consola, ingresar_producto, imprimir_inventario, retornar_precio_producto
from SingletonInventario import Inventario
from Venta import Venta

# Inicio del programa
if __name__ == "__main__":

    # Inicialización de instancias y variables
    inventario = Inventario()
    inventario.inicializacion()
    venta = Venta()
    opcion = 1

    # Este ciclo infinito permitirá consultar permanentemente las opciones del menú
    # El bucle solo puede terminar cuando se ingrese 0 en las opciones del menú
    while opcion != 0:

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

            tipo_producto = int(input('Para ingresar Fruta escriba 1, o para ingresar Verdura escriba 2 -> '))

            nombre_producto = str(input('Ingrese el nombre del producto -> '))

            precio_producto = int(input('Ingrese el precio unitario del producto -> '))

            cantidad_producto = int(input('Ingrese la cantidad del producto -> '))

            # De acuerdo al tipo de producto seleccionado se elige una opción o se presenta un error en consola
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

            mensaje = imprimir_inventario(inventario)
            print( mensaje )
            input('Ingrese Enter para continuar')

        # Realizar una venta a un cliente
        elif opcion == 3:

            codigo_producto = ""

            # Se llama este método de la clase para reiniciar los valores de la factura de venta
            # cada vez que se atienda un cliente nuevo
            venta.preparar_nueva_venta()

            # Permite actualizar la factura de venta y permitir al usuario agregar más productos hasta que
            # ingrese la opción xx
            while codigo_producto != "xx":

                limpiar_consola()
                mensaje = imprimir_inventario(inventario)
                print(mensaje)
                codigo_producto = input('Ingrese el código de venta del producto que desea comprar, o xx para proceder a pagar -> ')

                # Se llama esta función para buscar el producto en el inventario y retornar el costo del producto
                precio_producto = retornar_precio_producto( inventario, codigo_producto )

                # Se llama al método acumular venta para ir agregando el costo a la factura
                venta.acumular_venta(precio_producto)

                limpiar_consola()
                print("==================================================")
                print(f'Valor actual factura: {venta.retorna_valor_venta()}')
                print("==================================================\n")
                input('Ingrese Enter para continuar')

            limpiar_consola()

            # Se procede a preguntar al usuario si es estudiante o docente para aplicar descuento
            opcion_descuento = int(input('Si usted es estudiante o docente ingrese 1, en caso contrario ingrese 0 -> '))

            print("==================================================")
            print(f'Valor actual factura: {venta.retorna_valor_venta()}')
            print("==================================================\n")

            # Se verifica si el usuario es beneficiario de descuento
            if opcion_descuento == 1:

                # Internamente en la clase se aplica el descuento a la venta con el atributo de la instancia
                venta.aplicar_descuento()

                print("==================================================")
                print(f'El valor total de la factura aplicando el descuento del 5% es: {venta.retorna_valor_venta()}')
                print("==================================================\n")
            else:
                print("==================================================")
                print(f'No es beneficiario de descuentos en su factura')
                print("==================================================\n")

            input('Ingrese Enter para continuar')

        # Salir del sistema
        elif opcion == 0:
            limpiar_consola()
            print('Fin de la jornada en la tienda!!!!')

        # Error de ingreso
        else:
            print('Opción incorrecta, intente de nuevo!!!')
