# servicios/biblioteca_servicio.py

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Contiene la lógica del negocio del sistema.
    """

    def __init__(self):
        # Diccionario obligatorio: ISBN -> Libro
        self.__libros_disponibles = {}

        # Diccionario para usuarios
        self.__usuarios = {}

        # Set obligatorio para IDs únicos
        self.__ids_usuarios = set()

    # ===============================
    # Gestión de Libros
    # ===============================

    def añadir_libro(self, titulo, autor, categoria, isbn):
        if isbn in self.__libros_disponibles:
            print("❌ Ya existe un libro con ese ISBN.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.__libros_disponibles[isbn] = libro
        print("✅ Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.__libros_disponibles:
            del self.__libros_disponibles[isbn]
            print("✅ Libro eliminado.")
        else:
            print("❌ Libro no encontrado.")

    # ===============================
    # Gestión de Usuarios
    # ===============================

    def registrar_usuario(self, nombre, user_id):
        if user_id in self.__ids_usuarios:
            print("❌ ID de usuario ya existe.")
            return

        usuario = Usuario(nombre, user_id)
        self.__usuarios[user_id] = usuario
        self.__ids_usuarios.add(user_id)
        print("✅ Usuario registrado correctamente.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.__usuarios:
            del self.__usuarios[user_id]
            self.__ids_usuarios.remove(user_id)
            print("✅ Usuario dado de baja.")
        else:
            print("❌ Usuario no encontrado.")

    # ===============================
    # Préstamos
    # ===============================

    def prestar_libro(self, user_id, isbn):
        if user_id not in self.__usuarios:
            print("❌ Usuario no existe.")
            return

        if isbn not in self.__libros_disponibles:
            print("❌ Libro no disponible.")
            return

        usuario = self.__usuarios[user_id]
        libro = self.__libros_disponibles.pop(isbn)

        usuario.prestar_libro(libro)
        print("✅ Libro prestado correctamente.")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.__usuarios:
            print("❌ Usuario no existe.")
            return

        usuario = self.__usuarios[user_id]

        for libro in usuario.get_libros_prestados():
            if libro.get_isbn() == isbn:
                usuario.devolver_libro(libro)
                self.__libros_disponibles[isbn] = libro
                print("✅ Libro devuelto correctamente.")
                return

        print("❌ El usuario no tiene ese libro.")

    # ===============================
    # Búsquedas
    # ===============================

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.__libros_disponibles.values()
                if libro.get_titulo().lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.__libros_disponibles.values()
                if libro.get_autor().lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.__libros_disponibles.values()
                if libro.get_categoria().lower() == categoria.lower()]

    def listar_libros_usuario(self, user_id):
        if user_id not in self.__usuarios:
            print("❌ Usuario no existe.")
            return []

        return self.__usuarios[user_id].get_libros_prestados()
    