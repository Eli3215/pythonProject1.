# Importación de módulos
from os import system

# Esta función permite limpiar la consola
# Parámetros de entrada: Ninguno
# Retorna: No
def limpiar_consola():
    system('cls')

# Esta función permite mostrar el menú al administrador de la caja registradora
# Parámetros de entrada: Ninguno
# Retorna: La opción para continuar con las opciones en caja
def mostrar_menu_administrador():
    print('Hola administrador, seleccione la acción que desea realizar:')
    print('1. Ingresar productos al inventario')
    print('2. Realizar una venta a un cliente')
    print('3. Salir')
    print('****************************************')

    opcion = int(input('Ingrese la opción a realizar -> '))
    return opcion

# Inicio del programa
if __name__ == "__main__":

    # Este ciclo infinito permitirá consultar permanentemente las opciones del menú
    # en la caja registradora
    while True:
        limpiar_consola()
        opcion = mostrar_menu_administrador()

        # En este condicional se verifica si ya no se desean realizar más acciones para salir del sistema
        if opcion == 3:
            limpiar_consola()
            print('Fin de la jornada en la tienda!!!!')
            break