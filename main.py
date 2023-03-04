mensaje = "Primer programa para verificar que PyCharm está bien instalado"

if __name__ == '__main__':
    print( mensaje )
from os import system
from time import sleep


def limpiar_consola():
    system('cls')


for i in range(5):
    print(f"Borrando la consola con cada ejecución!! {i+1}")
    sleep(1)
    limpiar_consola()
