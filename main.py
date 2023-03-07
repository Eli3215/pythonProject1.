# Importación de módulos
from funciones import mostrar_menu_administrador, limpiar_consola, computar_producto
from time import sleep

# Inicio del programa
if __name__ == "__main__":

    # Este ciclo infinito permitirá consultar permanentemente las opciones del menú
    # en la caja registradora
    while True:
        limpiar_consola()
        opcion = mostrar_menu_administrador()

        if opcion == 1:
            print('Ingresando producto al inventario')

        elif opcion == 2:
            computar_producto()

        elif opcion == 3:
            limpiar_consola()
            print('Fin de la jornada en la tienda!!!!')
            break

        else:
            print('Opción incorrecta, intente de nuevo!!!')

        sleep(3) # Se espera unos segundos para actualizar la consola

