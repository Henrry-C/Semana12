# Este proyecto consiste en el desarrollo de un Sistema de Gestión de Biblioteca Digital aplicando:

Programación Orientada a Objetos (POO)

Arquitectura estructurada por capas

Separación clara entre modelos, servicios y punto de entrada

El sistema permite administrar libros, usuarios y préstamos mediante un menú interactivo en consola.

biblioteca_app/│
 modelos/
 libro.py
    usuario.py

 servicios/
    biblioteca_servicio.py

main.py

Capa Modelos (modelos/)

Contiene las clases que representan las entidades del sistema:

Libro

Usuario

 Capa Servicios (servicios/)

Contiene la lógica del negocio:

Gestión de libros

Registro de usuarios

Préstamos y devoluciones

Búsquedas

 Punto de Entrada (main.py)

Contiene el menú interactivo en consola.
No incluye lógica de negocio, únicamente interactúa con la capa de servicios.

 Principios Aplicados

Encapsulamiento mediante atributos privados

Separación de responsabilidades

Arquitectura por capas

Uso correcto de estructuras de datos

Métodos organizados y coherentes

 Modelos del Sistema
 Clase Libro

Representa un libro dentro del sistema.

Atributos:

Título y autor almacenados en una tupla (inmutable)

Categoría

ISBN (identificador único)

Decisión técnica:
Se utiliza una tupla para garantizar la inmutabilidad del título y autor.

 Clase Usuario

Representa un usuario registrado.

Atributos:

Nombre

ID único

Lista de libros prestados

Decisión técnica:
Se utiliza una lista para almacenar los libros prestados.

 BibliotecaServicio

Clase encargada de la lógica del sistema.

Estructuras de datos utilizadas (requisitos obligatorios):

 Diccionario para libros disponibles

Clave: ISBN

Valor: Objeto Libro

 Diccionario para usuarios registrados

 Set para garantizar IDs únicos de usuarios

 Funcionalidades Implementadas

El sistema permite:

Añadir libros

Quitar libros

Registrar usuarios

Dar de baja usuarios

Prestar libros

Devolver libros

Buscar libros por:

Título

Autor

Categoría

Listar libros prestados por usuario

 Cómo Ejecutar el Proyecto

Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>

Ingresar a la carpeta:

cd biblioteca_app

Ejecutar el sistema:

python main.py
 Pruebas del Sistema

El funcionamiento puede comprobarse mediante:

Registro de usuarios

Añadir libros

Realizar préstamos

Devoluciones

Búsquedas en el catálogo

Listado de libros prestados

El sistema se ejecuta completamente desde main.py.

 Objetivo Académico

Este proyecto demuestra:

Correcta aplicación de Programación Orientada a Objetos

Uso adecuado de estructuras de datos (tupla, lista, diccionario y set)

Separación clara entre modelo y lógica de negocio

Implementación de un sistema funcional en consola

 Autor

Henry David Coello Irua
Curso: Programación Orientada a Objetos
Semana 12
