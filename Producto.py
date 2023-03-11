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
    def establecer_codigo_producto(self) -> None:
        pass

    @abstractmethod
    def establecer_cantidad_producto(self, cantidad) -> None:
        pass

    @abstractmethod
    def retornar_nombre_producto(self) -> str:
        pass

    @abstractmethod
    def retornar_precio_producto(self) -> float:
        pass

    @abstractmethod
    def retornar_codigo_producto(self) -> int:
        pass

    @abstractmethod
    def retornar_cantidad_producto(self) -> int:
        pass

# Los productos de cada categoría proporcionan diferentes implementaciones de la interfaz Producto
class Fruta(Producto):

    codigo_producto = 0

    def establecer_nombre_producto(self, nombre) -> None:
        self.nombre = nombre

    def establecer_precio_producto(self, precio) -> None:
        self.precio = precio

    def establecer_codigo_producto(self) -> None:
        Fruta.codigo_producto = Fruta.codigo_producto + 1
        self.codigo = "f" + str(Fruta.codigo_producto)

    def establecer_cantidad_producto(self, cantidad) -> None:
        self.cantidad = cantidad

    def retornar_nombre_producto(self) -> str:
        return self.nombre

    def retornar_precio_producto(self) -> float:
        return self.precio

    def retornar_codigo_producto(self) -> str:
        return self.codigo

    def retornar_cantidad_producto(self) -> int:
        return self.cantidad

class Verdura(Producto):

    codigo_producto = 0

    def establecer_nombre_producto(self, nombre) -> None:
        self.nombre = nombre

    def establecer_precio_producto(self, precio) -> None:
        self.precio = precio

    def establecer_codigo_producto(self) -> None:
        Verdura.codigo_producto = Verdura.codigo_producto + 1
        self.codigo = "v" + str(Verdura.codigo_producto)

    def establecer_cantidad_producto(self, cantidad) -> None:
        self.cantidad = cantidad

    def retornar_nombre_producto(self) -> str:
        return self.nombre

    def retornar_precio_producto(self) -> float:
        return self.precio

    def retornar_codigo_producto(self) -> str:
        return self.codigo

    def retornar_cantidad_producto(self) -> int:
        return self.cantidad

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


