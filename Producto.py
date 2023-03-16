# Importación de modulos
from abc import ABC, abstractmethod

# Interfaz del Producto que declara las operaciones que todos los Productos concretos deben implementar
class Producto(ABC):

    # Método para establecer el nombre del producto
    # Parámetros de ingreso: nombre del producto
    # Retorna: No
    @abstractmethod
    def establecer_nombre_producto(self, nombre) -> None:
        pass

    # Método para establecer el precio del producto
    # Parámetros de ingreso: Precio del producto
    # Retorna: No
    @abstractmethod
    def establecer_precio_producto(self, precio) -> None:
        pass

    # Método para establecer el código del producto
    # Parámetros de ingreso: No
    # Retorna: No
    @abstractmethod
    def establecer_codigo_producto(self) -> None:
        pass

    # Método para establecer la cantidad de elementos del producto
    # Parámetros de ingreso: Cantidad del producto
    # Retorna: No
    @abstractmethod
    def establecer_cantidad_producto(self, cantidad) -> None:
        pass

    # Método para retornar el nombre del producto
    # Parámetros de ingreso: No
    # Retorna: Nombre del producto
    @abstractmethod
    def retornar_nombre_producto(self) -> str:
        pass

    # Método para retornar el precio del producto
    # Parámetros de ingreso: No
    # Retorna: Precio del producto
    @abstractmethod
    def retornar_precio_producto(self) -> float:
        pass

    # Método para retornar el código del producto
    # Parámetros de ingreso: No
    # Retorna: Código del producto
    @abstractmethod
    def retornar_codigo_producto(self) -> int:
        pass

    # Método para retornar la cantidad de elementos del producto
    # Parámetros de ingreso: No
    # Retorna: Cantidad de elementos del producto
    @abstractmethod
    def retornar_cantidad_producto(self) -> int:
        pass

# Se implementan los métodos abstractos de la interfaz Producto en la clase Fruta
class Fruta(Producto):

    # Variable de clase para establecer el código del producto
    codigo_producto = 0

    # Método para establecer el nombre del producto
    # Parámetros de ingreso: Nombre del producto
    # Retorna: No
    def establecer_nombre_producto(self, nombre) -> None:
        self.nombre = nombre

    # Método para establecer el precio del producto
    # Parámetros de ingreso: Precio del producto
    # Retorna: No
    def establecer_precio_producto(self, precio) -> None:
        self.precio = precio

    # Método para establecer el código del producto
    # Parámetros de ingreso: No
    # Retorna: No
    def establecer_codigo_producto(self) -> None:
        Fruta.codigo_producto = Fruta.codigo_producto + 1
        self.codigo = "f" + str(Fruta.codigo_producto)

    # Método para establecer la cantidad de elementos del producto
    # Parámetros de ingreso: Cantidad de elementos del producto
    # Retorna: No
    def establecer_cantidad_producto(self, cantidad) -> None:
        self.cantidad = cantidad

    # Método para retornar el nombre del producto
    # Parámetros de ingreso: No
    # Retorna: Nombre del producto
    def retornar_nombre_producto(self) -> str:
        return self.nombre

    # Método para retornar el precio del producto
    # Parámetros de ingreso: No
    # Retorna: Precio del producto
    def retornar_precio_producto(self) -> float:
        return self.precio

    # Método para retornar el código del producto
    # Parámetros de ingreso: No
    # Retorna: Código del producto
    def retornar_codigo_producto(self) -> str:
        return self.codigo

    # Método para retornar la cantidad de elementos del producto
    # Parámetros de ingreso: No
    # Retorna: Cantidad de elementos del producto
    def retornar_cantidad_producto(self) -> int:
        return self.cantidad

# Se implementan los métodos abstractos de la interfaz Producto en la clase Verdura
class Verdura(Producto):

    # Variable de clase para establecer el código del producto
    codigo_producto = 0

    # Método para establecer el nombre del producto
    # Parámetros de ingreso: Nombre del producto
    # Retorna: No
    def establecer_nombre_producto(self, nombre) -> None:
        self.nombre = nombre

    # Método para establecer el precio del producto
    # Parámetros de ingreso: Precio del producto
    # Retorna: No
    def establecer_precio_producto(self, precio) -> None:
        self.precio = precio

    # Método para establecer el código del producto
    # Parámetros de ingreso: No
    # Retorna: No
    def establecer_codigo_producto(self) -> None:
        Verdura.codigo_producto = Verdura.codigo_producto + 1
        self.codigo = "v" + str(Verdura.codigo_producto)

    # Método para establecer la cantidad de elementos del producto
    # Parámetros de ingreso: Cantidad de elementos del producto
    # Retorna: No
    def establecer_cantidad_producto(self, cantidad) -> None:
        self.cantidad = cantidad

    # Método para retornar el nombre del producto
    # Parámetros de ingreso: No
    # Retorna: Nombre del producto
    def retornar_nombre_producto(self) -> str:
        return self.nombre

    # Método para retornar el precio del producto
    # Parámetros de ingreso: No
    # Retorna: Precio del producto
    def retornar_precio_producto(self) -> float:
        return self.precio


    # Método para retornar el código del producto
    # Parámetros de ingreso: No
    # Retorna: Código del producto
    def retornar_codigo_producto(self) -> str:
        return self.codigo

    # Método para retornar la cantidad de elementos del producto
    # Parámetros de ingreso: No
    # Retorna: Cantidad de elementos del producto
    def retornar_cantidad_producto(self) -> int:
        return self.cantidad

# Esta clase Factory declara el método factory que retornará un objeto de la clase Producto.
class Factory:

    # Este método permite returnar un objeto ya sea de la clase Fruta o de la clase Verdura
    # Parámetros de ingreso: Tipo de producto a ser generado ('Fruta' o 'Verdura')
    # Retorna: Instancia de la clase Fruta() o de la clase Verdura()
    def crear_producto(self, tipo_producto) -> Producto:
        if tipo_producto == 'Fruta':
            return Fruta()
        elif tipo_producto == 'Verdura':
            return Verdura()
        else:
            print('Error')
            return None


