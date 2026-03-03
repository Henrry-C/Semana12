# modelos/usuario.py

class Usuario:
    """
    Representa un usuario registrado en la biblioteca.
    """

    def __init__(self, nombre, user_id):
        self.__nombre = nombre
        self.__user_id = user_id
        # Lista para libros prestados (requisito obligatorio)
        self.__libros_prestados = []

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_user_id(self):
        return self.__user_id

    def get_libros_prestados(self):
        return self.__libros_prestados

    # Métodos de gestión de préstamos
    def prestar_libro(self, libro):
        self.__libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.__nombre} | ID: {self.__user_id}"
    