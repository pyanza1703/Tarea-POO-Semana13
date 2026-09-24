import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, master, servicio_restaurante, usuario_actual, al_cerrar_sesion):
        super().__init__(master)
        self.master = master
        self.servicio = servicio_restaurante
        self.usuario = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.master.title("Restaurante App - Panel Principal")
        self.master.geometry("680x460")

        self._crear_widgets()

    def _crear_widgets(self):
        frame_top = tk.Frame(self, bg="#ECEFF1", height=40)
        frame_top.pack(fill="x", side="top")

        lbl_user = tk.Label(
            frame_top,
            text=f"Sesión activa: {self.usuario.nombre} ({self.usuario.usuario})",
            font=("Arial", 9, "bold"), bg="#ECEFF1"
        )
        lbl_user.pack(side="left", padx=12, pady=8)

        btn_logout = tk.Button(
            frame_top, text="Cerrar Sesión", font=("Arial", 8, "bold"),
            bg="#E53935", fg="white", command=self.al_cerrar_sesion
        )
        btn_logout.pack(side="right", padx=12, pady=6)

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        frame_productos = tk.Frame(notebook)
        notebook.add(frame_productos, text=" Productos Registrados ")
        self._construir_tabla_productos(frame_productos)

        frame_usuarios = tk.Frame(notebook)
        notebook.add(frame_usuarios, text=" Usuarios Registrados ")
        self._construir_tabla_usuarios(frame_usuarios)

        frame_ventas = tk.Frame(notebook)
        notebook.add(frame_ventas, text=" Ventas (Pendiente) ")
        self._construir_vista_ventas_pendiente(frame_ventas)

    def _construir_tabla_productos(self, parent):
        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        tree = ttk.Treeview(parent, columns=columnas, show="headings")

        tree.heading("codigo", text="Código")
        tree.heading("nombre", text="Nombre")
        tree.heading("categoria", text="Categoría")
        tree.heading("precio", text="Precio ($)")
        tree.heading("stock", text="Stock")

        tree.column("codigo", width=80, anchor="center")
        tree.column("nombre", width=180, anchor="w")
        tree.column("categoria", width=120, anchor="w")
        tree.column("precio", width=90, anchor="e")
        tree.column("stock", width=70, anchor="center")

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        productos = self.servicio.obtener_productos()
        for p in productos:
            precio_fmt = f"${p.precio:.2f}" if isinstance(p.precio, (int, float)) else str(p.precio)
            tree.insert("", "end", values=(p.codigo, p.nombre, p.categoria, precio_fmt, p.stock))

    def _construir_tabla_usuarios(self, parent):
        columnas = ("identificador", "nombre", "usuario")
        tree = ttk.Treeview(parent, columns=columnas, show="headings")

        tree.heading("identificador", text="Identificador")
        tree.heading("nombre", text="Nombre")
        tree.heading("usuario", text="Usuario")

        tree.column("identificador", width=100, anchor="center")
        tree.column("nombre", width=220, anchor="w")
        tree.column("usuario", width=160, anchor="w")

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            tree.insert("", "end", values=(u.identificador, u.nombre, u.usuario))

    def _construir_vista_ventas_pendiente(self, parent):
        lbl_msg = tk.Label(
            parent,
            text="MÓDULO DE VENTAS EN DESARROLLO\n\nFuncionalidad identificada como pendiente",
            font=("Arial", 11, "italic"), fg="gray"
        )
        lbl_msg.pack(expand=True)