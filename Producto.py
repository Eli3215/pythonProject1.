from abc import ABC, abstractmethod

# Interfaz del Producto que declara las operaciones que todos los Productos concretos deben implementar
class Producto(ABC):

    @abstractmethod
    def establecer_nombre_producto(self, nombre) -> None:
        pass

    @abstractmethod
    def establecer_precio_producto(self, precio) -> None:
        pass

    @abstractmethod
    def venta_producto(self) -> str:
        pass

# Los productos de cada categoría proporcionan diferentes implementaciones de la interfaz Producto
class Fruta(Producto):

    def establecer_nombre_producto(self, nombre) -> None:
        self.nombre = nombre

    def establecer_precio_producto(self, precio) -> None:
        self.precio = precio

    def venta_producto(self) -> str:
        return f"La fruta {self.nombre} tiene un precio de {self.precio}"

class Verdura(Producto):

    def establecer_nombre_producto(self, nombre) -> None:
        self.nombre = nombre

    def establecer_precio_producto(self, precio) -> None:
        self.precio = precio

    def venta_producto(self) -> str:
        return f"La verdura {self.nombre} tiene un precio de {self.precio}"

# Esta clase Factory declara el método factory que retornará un objeto de la clase Producto.

class Factory:

    def crear_producto(self, tipo_producto) -> Producto:
        if tipo_producto == 'Fruta':
            return Fruta()
        elif tipo_producto == 'Verdura':
            return Verdura()
        else:
            print('Error')
            return None


