class Venta:

    def __init__(self):
        self.numero_cliente = 0
        self.valor_venta = 0

    # Esta función calcula el precio de venta de la factura y se acumula en el atributo valor_venta
    # Parámetros de ingreso: se ingresa el valor del nuevo producto vendido
    # Retorna: No
    def acumular_venta(self, valor_nuevo_producto_vendido) -> None:
        self.valor_venta = self.valor_venta + valor_nuevo_producto_vendido

    # Esta función se encarga de aplicar el descuento a la venta y de recalcular el valor total de la venta
    # Parámetros de ingreso: No
    # Retorna: No
    def aplicar_descuento(self) -> None:
        self.valor_venta = self.valor_venta - ((self.valor_venta * 5.0) / 100.0)

    # Esta función se encarga de retornar el valor de la venta
    # Parámetros de ingreso: No
    # Retorna: Se retorna el valor de la venta ya sea con o sin descuento
    def retorna_valor_venta(self) -> float:
        return self.valor_venta

    # Esta función se encarga de reinicializar a cero el acumulador de precio de venta
    # Parámetros de ingreso: No
    # Retorna: No
    def preparar_nueva_venta(self) -> None:
        self.valor_venta = 0
