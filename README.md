# Sistema de Gestión de Restaurante - Semana 13 (`restaurante_app`)

**Autor:** Pablo Javier Yanza Delgado  
**Materia:** Programación Orientada a Objetos (POO)  

---

## 📄 Descripción del Proyecto
Este proyecto corresponde a la **Semana 13** de la asignatura **Programación Orientada a Objetos (POO)**. En esta entrega se realiza la migración de la aplicación de consola hacia una **Interfaz Gráfica de Usuario (GUI)** desarrollada mediante la librería nativa **Tkinter** en Python.

La aplicación aplica una arquitectura modular limpia por capas (Modelos, Servicios, Datos y UI) operando bajo una **ventana única de ejecución** que alterna sus vistas (Login y Panel Principal) sin abrir ventanas emergentes secundarias ni duplicar instancias.

### 🔑 Credenciales de Prueba (Simulación)

El modelo de datos implementa encapsulamiento mediante decoradores `@property` y `@setter`, validando la presencia de datos en cada atributo:

* **`usuario`**: Nombre de usuario o credencial de acceso (ej. `"admin"` o `"0912345678"`).
* **`contrasena`** / **`contraseña`**: Clave de acceso asociada al usuario para la autenticación en el sistema.

        "usuario": "admin",
        "contraseña": "1234"

        "usuario": "0912345678",
        "contraseña": "1234"
    
---

## 🏗️ Estructura del Repositorio

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md