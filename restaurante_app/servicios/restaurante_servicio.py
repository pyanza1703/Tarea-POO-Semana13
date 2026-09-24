import os
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS_DIR = os.path.join(BASE_DIR, "datos")

class RestauranteServicio:
    def __init__(self):
        self._productos = []
        self._usuarios = []
        self._indice_usuarios = {}
        self.cargar_datos()

    def cargar_datos(self):
        ruta_p = os.path.join(DATOS_DIR, "productos.json")
        ruta_u = os.path.join(DATOS_DIR, "usuarios.json")

        self._productos = ArchivoServicio.cargar_json(ruta_p, Producto)
        self._usuarios = ArchivoServicio.cargar_json(ruta_u, Usuario)
        self._indice_usuarios = {u.identificador: u for u in self._usuarios}

    def validar_acceso(self, usuario_input: str, clave_input: str):
        if not usuario_input or not clave_input:
            return False, "Por favor complete todos los campos.", None

        for u in self._usuarios:
            if u.usuario == usuario_input or u.nombre.lower() == usuario_input.lower():
                if u.contrasena == clave_input:
                    return True, f"Bienvenido/a {u.nombre}", u
                else:
                    return False, "Contraseña incorrecta.", None

        return False, "Usuario no encontrado.", None

    def obtener_productos(self):
        return self._productos

    def obtener_usuarios(self):
        return self._usuarios