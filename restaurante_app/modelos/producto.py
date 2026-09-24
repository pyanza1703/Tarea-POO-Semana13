class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int, categoria: str = ""):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            codigo=data.get("codigo", ""),
            nombre=data.get("nombre", ""),
            precio=float(data.get("precio", 0.0)),
            stock=int(data.get("stock", 0)),
            categoria=data.get("categoria", "")
        )