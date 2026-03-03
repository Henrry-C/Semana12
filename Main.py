# main.py

from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA DIGITAL =====")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro por título")
    print("8. Buscar libro por autor")
    print("9. Buscar libro por categoría")
    print("10. Listar libros prestados de un usuario")
    print("0. Salir")


def main():
    biblioteca = BibliotecaServicio()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.añadir_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")
            biblioteca.registrar_usuario(nombre, user_id)

        elif opcion == "4":
            user_id = input("ID del usuario: ")
            biblioteca.dar_baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            titulo = input("Título: ")
            resultados = biblioteca.buscar_por_titulo(titulo)
            for libro in resultados:
                print(libro)

        elif opcion == "8":
            autor = input("Autor: ")
            resultados = biblioteca.buscar_por_autor(autor)
            for libro in resultados:
                print(libro)

        elif opcion == "9":
            categoria = input("Categoría: ")
            resultados = biblioteca.buscar_por_categoria(categoria)
            for libro in resultados:
                print(libro)

        elif opcion == "10":
            user_id = input("ID del usuario: ")
            libros = biblioteca.listar_libros_usuario(user_id)
            for libro in libros:
                print(libro)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
    