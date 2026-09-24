import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, master, servicio_restaurante, al_ingresar_exitoso):
        super().__init__(master)
        self.master = master
        self.servicio = servicio_restaurante
        self.al_ingresar_exitoso = al_ingresar_exitoso

        self.master.title("Restaurante App - Acceso")
        self.master.geometry("380x300")
        self.master.resizable(False, False)

        self._crear_widgets()

    def _crear_widgets(self):
        lbl_titulo = tk.Label(self, text="SISTEMA DE RESTAURANTE", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=20)

        lbl_user = tk.Label(self, text="Usuario / ID:", font=("Arial", 10))
        lbl_user.pack(anchor="w", padx=45)
        self.txt_usuario = tk.Entry(self, font=("Arial", 10), width=30)
        self.txt_usuario.pack(pady=2)

        lbl_pass = tk.Label(self, text="Contraseña:", font=("Arial", 10))
        lbl_pass.pack(anchor="w", padx=45, pady=(10, 0))
        self.txt_clave = tk.Entry(self, font=("Arial", 10), width=30, show="*")
        self.txt_clave.pack(pady=2)


        btn_ingresar = tk.Button(
            self, text="Iniciar Sesión", font=("Arial", 10, "bold"),
            bg="#2196F3", fg="white", width=18, command=self._ejecutar_login
        )
        btn_ingresar.pack(pady=12)

    def _ejecutar_login(self):
        user = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        exito, mensaje, usuario_obj = self.servicio.validar_acceso(user, clave)

        if exito:
            messagebox.showinfo("Acceso Exitoso", mensaje)
            self.al_ingresar_exitoso(usuario_obj)
        else:
            messagebox.showerror("Error de Acceso", mensaje)