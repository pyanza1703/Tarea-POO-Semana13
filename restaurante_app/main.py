import sys
import os
import tkinter as tk

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class AplicacionRestaurante:
    def __init__(self, root):
        self.root = root
        self.servicio = RestauranteServicio()
        self.mostrar_login()

    def mostrar_login(self):
        self._limpiar_ventana()
        self.vista_login = LoginView(self.root, self.servicio, self.al_login_exitoso)
        self.vista_login.pack(fill="both", expand=True)

    def al_login_exitoso(self, usuario):
        self._limpiar_ventana()
        self.vista_principal = MainView(self.root, self.servicio, usuario, self.mostrar_login)
        self.vista_principal.pack(fill="both", expand=True)

    def _limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = AplicacionRestaurante(root)
    root.mainloop()

if __name__ == "__main__":
    main()