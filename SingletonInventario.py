from Producto import Fruta, Verdura

class SingletonInventarioMeta(type):

    _instancias = {}

    # Este método es el que restringe que solo se pueda crear una instancia del objeto
    def __call__(cls, *args, **kwargs):

        if cls not in cls._instancias:
            instancia = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instancia
        return cls._instancias[cls]


class Inventario(metaclass=SingletonInventarioMeta):

    # Esta función permite inicializar los vectores donde se almacenarán los productos por categorías
    # Parámetros de ingreso: Ninguno
    # Retorna: No
    def inicializacion(self) -> None:
        self.inventario_frutas = [] # Arreglo donde se almacenan las frutas
        self.inventario_verduras = [] # Arreglo donde se almacenan las verduras

    # Esta función permite agregar una Fruta al inventario de frutas
    # Parámetros de ingreso: Recibe un producto tipo Fruta
    # Retorna: No
    def agregar_fruta(self, producto) -> None:
        self.inventario_frutas.append(producto)

    # Esta función permite agregar una Verdura al inventario de verduras
    # Parámetros de ingreso: Recibe un producto tipo Verdura
    # Retorna: No
    def agregar_verdura(self, producto) -> None:
        self.inventario_verduras.append(producto)

    # Esta función permite retornar una Fruta que esté en el inventario
    # Parámetros de ingreso: codigo de la fruta
    # Retorna: Si se encuentra la fruta se retorna, en caso contrario se retorna None
    def retornar_Fruta(self, codigo_producto) -> Fruta:

        fruta = None
        cantidad_elementos_arreglo = len(self.inventario_frutas)
        for index in range( cantidad_elementos_arreglo ):
            if self.inventario_frutas[index].retornar_codigo_producto() == codigo_producto:

                actualizar_cantidad_producto_en_inventario = self.inventario_frutas[index].retornar_cantidad_producto() - 1

                if actualizar_cantidad_producto_en_inventario >= 0:
                    self.inventario_frutas[index].establecer_cantidad_producto( actualizar_cantidad_producto_en_inventario )
                    fruta = self.inventario_frutas[index]

            if self.inventario_frutas[index].retornar_cantidad_producto() == 0:
                self.inventario_frutas.pop(index)
                break

        return fruta

    # Esta función permite retornar una Verdura que esté en el inventario
    # Parámetros de ingreso: codigo de la verdura
    # Retorna: Si se encuentra la verdura se retorna, en caso contrario se retorna None
    def retornar_Verdura(self, codigo_producto) -> Verdura:

        verdura = None
        cantidad_elementos_arreglo = len(self.inventario_verduras)
        for index in range(cantidad_elementos_arreglo):
            if self.inventario_verduras[index].retornar_codigo_producto() == codigo_producto:

                actualizar_cantidad_producto_en_inventario = self.inventario_verduras[
                                                                 index].retornar_cantidad_producto() - 1

                if actualizar_cantidad_producto_en_inventario >= 0:
                    self.inventario_verduras[index].establecer_cantidad_producto(
                        actualizar_cantidad_producto_en_inventario)
                    verdura = self.inventario_verduras[index]

            if self.inventario_verduras[index].retornar_cantidad_producto() == 0:
                self.inventario_verduras.pop(index)
                break

        return verdura

    # Esta función permite imprimir el inventario de Frutas y Verduras disponibles.
    # Parámetros de ingreso: Ninguno
    # Retorna: El mensaje para imprimir en consola
    def imprimir_inventario(self) -> str:

        # Definimos una variable de tipo str para imprimir el inventario de productos
        # en forma de tabla
        mensaje =  "=================================================================================\n"
        mensaje += "=====                            INVENTARIO TIENDA                          =====\n"
        mensaje += "=================================================================================\n"
        mensaje += "|\tCódigo\t|\tTipo\t|\tNombre\t|\tPrecio\t|    Cantidad   |\n"
        mensaje += "=================================================================================\n"
        for f in self.inventario_frutas:
            mensaje += "|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\t|\n".format(f.retornar_codigo_producto(), "Fruta", f.retornar_nombre_producto(), f.retornar_precio_producto(), f.retornar_cantidad_producto())

        mensaje += "=================================================================================\n"

        for f in self.inventario_verduras:
            mensaje += "|\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|\t{4}\t|\n".format(f.retornar_codigo_producto(), "Verdura", f.retornar_nombre_producto(), f.retornar_precio_producto(), f.retornar_cantidad_producto())

        mensaje += "=================================================================================\n"

        return mensaje

    def actualizar_productos_disponibles_en_estanteria(self) -> str:

        productos_en_estanteria = [
            [], # En esta fila se agregan las frutas
            []  # En esta fila se agregan las verduras
        ]
        for f in self.inventario_frutas:
            for _ in range(f.retornar_cantidad_producto()):
                productos_en_estanteria[0].append(f.retornar_nombre_producto())

        for f in self.inventario_verduras:
            for _ in range(f.retornar_cantidad_producto()):
                productos_en_estanteria[1].append(f.retornar_nombre_producto())

        mensaje  = "\n=============================================================================\n"
        mensaje += "\n|  SELECCIONE SU PRODUCTO DEL ESTANTE DE ACUERDO AL CODIGO DE LA TABLA\n"
        mensaje += "\n=============================================================================\n"
        for categoria in productos_en_estanteria:

            for producto in categoria:

                mensaje += producto + " | "

            mensaje += "\n=============================================================================\n"

        return mensaje
