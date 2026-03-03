# modelos/libro.py

class Libro:
    """
    Representa un libro dentro del sistema de biblioteca.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable para título y autor (requisito obligatorio)
        self.__info = (titulo, autor)
        self.__categoria = categoria
        self.__isbn = isbn

    # Getters (encapsulamiento)
    def get_titulo(self):
        return self.__info[0]

    def get_autor(self):
        return self.__info[1]

    def get_categoria(self):
        return self.__categoria

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f"Título: {self.get_titulo()} | Autor: {self.get_autor()} | Categoría: {self.__categoria} | ISBN: {self.__isbn}"
    