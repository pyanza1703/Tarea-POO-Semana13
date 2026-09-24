import json
import os

class ArchivoServicio:
    @staticmethod
    def cargar_json(ruta: str, clase_modelo):
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [clase_modelo.from_dict(d) for d in datos]
        except Exception as e:
            print(f"Error al cargar JSON ({ruta}): {e}")
            return []