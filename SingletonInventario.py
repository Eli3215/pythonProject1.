from Producto import Producto

class SingletonInventarioMeta(type):

    _instancias = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instancias:
            instancia = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instancia
        return cls._instancias[cls]

class Inventario(metaclass=SingletonInventarioMeta):

    def inicializacion(self):
        self.inventario_frutas = []
        self.inventario_verduras = []
        self.estanteria = []

    def agregar_fruta(self, producto: Producto) -> None:
        self.inventario_frutas.append(producto)

    def agregar_verdura(self, producto: Producto) -> None:
        self.inventario_verduras.append(producto)

    # Esta función permite imprimir el inventario de Frutas y Verduras disponibles.
    # Parámetros de ingreso: Ninguno
    # Retorna: No
    def imprimir_inventario(self) -> None:

        # Definimos una variable de tipo str para imprimir el inventario de productos
        # en forma de tabla
        mensaje = "--------------------------------------------------\n"
        mensaje += "-------          INVENTARIO TIENDA          ------\n"
        mensaje += "--------------------------------------------------\n"
        mensaje += "|\tTipo\t|\tNombre\t|\tPrecio\t|\n"
        mensaje += "--------------------------------------------------\n"
        for f in self.inventario_frutas:
            mensaje += "|\t{0}\t|\t{1}\t|\t{2}\t|\n".format("Fruta", f.nombre, f.precio)

        mensaje += "--------------------------------------------------\n"

        for f in self.inventario_verduras:
            mensaje += "|\t{0}\t|\t{1}\t|\t{2}\t|\n".format("Verdura", f.nombre, f.precio)

        mensaje += "--------------------------------------------------\n"
        print(mensaje)