import ejemplar as e
import prestamo as p
import sistema_biblio as sb
import usuario as u

import os.path as path
from pickle import dump, load

def crearLibros(sistema):
    print("\tAgregar libros al catálogo: ")
    aumentar = True
    reiniciar = True

    titulo = input("Ingrese Titulo: ")
    autor = input("Ingrese autor: ")
    editorial = input("Ingrese editorial: ")
    year = input("Ingrese año: ")

    ejemplares = int(input("Ingrese numero de ejemplares: "))
    miLibro = e.Ejemplar(titulo, autor, editorial, year, aumentar, ejemplares, reiniciar)
    sistema.add_Libros(miLibro)
    #print(miLibro)
    ejemplares = ejemplares - 1
    if ejemplares >= 1: #si hay más ejemplares entonces
        aumentar = False #Contador de Libro
        reiniciar = False #Reeiniciar contador de Ejemplar
        while ejemplares > 0: #crear el resto de los ejemplares
            miLibro = e.Ejemplar(titulo, autor, editorial, year, aumentar, ejemplares, reiniciar)
            sistema.add_Libros(miLibro)
            #print(miLibro)
            ejemplares = ejemplares - 1
        print("Se han agregado con exito los libros: \n{}".format( sistema.buscar_en_catalogo( miLibro.get_titulo() ) ) )
    else:
        print("Se ha agregado con exito el libro: \n{}".format( sistema.buscar_en_catalogo( miLibro.get_titulo() ) ) )
    return True

def crearUsuario(sistema):
    print("\nAgregar un nuevo usuario: ")
    nombre = input("Ingrese su nombre: ")
    user = u.Usuario(nombre)
    sistema.add_Usuario(user)
    print("¡{} se ha agregado con exito! Su id es {}".format(user.get_nombre(), user.get_id() ))
    return True

def verCatalogo(sistema):
    print("\tEl Catalogo se muestra a continuacion: ")
    #print(sistema.buscar_en_catalogo(""))
    return True

def buscarEnCatalogo(sistema):
    titulo = input("Ingrese el titulo que desea buscar: ")
    x = sistema.buscar_en_catalogo(titulo)
    if x == "":
        print("\tSu busqueda no coincide con nada.")
    else:
        print("\tSu busqueda coincide con: ")
        print(x)
    return True

def solicitarPrestamo(sistema):
    id_usuario = int(input("Ingrese su id de usuario: "))
    user = obtenerUsuarioPorID(sistema, id_usuario)

    if user == "":
        print("El usuario con id {} no existe".format(id_usuario))

    elif user.get_libros_en_prestamo() < 5:
        id_libro = float(input("Ingrese el id del libro que desea solicitar: "))
        ejemplar = obtenerEjemplarPorID(sistema, id_libro)

        if ejemplar == "":
            print("El ejemplar con id {} no existe.".format(id_libro))

        elif ejemplar.get_disponibilidad():
            tipo_prestamo = escogerTipoPrestamo()
            prestamo = p.Prestamo(tipo_prestamo, user, ejemplar)
            sistema.agregar_prestamo(prestamo)
            print("\n" + str(prestamo))
        else:
            print("Lo sentimos es ejemplar no está disponble")
    else:
        print("Lo sentimos, ha excedido su maximo de prestamos.")

    return True

def obtenerEjemplarPorID(sistema, id_libro):
    ejemplar = ""
    for libros in sistema.get_catalogo():
        x = "{}.{}".format(libros.get_id_libro(), libros.get_id())
        if str(id_libro) == x:
            ejemplar = libros
    return ejemplar

def obtenerUsuarioPorID(sistema, id_usuario):
    user = ""
    for usuarios in sistema.get_usuarios():
        if id_usuario == usuarios.get_id():
            user = usuarios
    return user


def escogerTipoPrestamo():
    tipo_prestamo = int(input("Tipo de prestamo: \n 1. Prestamo Regular: dos semanas\n 2. Prestamo Rapido: dos dias\nEscoja el numero del tipo de prestamo que desea: "))
    return tipo_prestamo


def cargarAlSistema(sistema):
    x = sistema
    nombre_archivo = input("\nIngrese el nombre del archivo que desea cargar: ")
    if path.exists(nombre_archivo):
        f = open(nombre_archivo, "rb")
        x = load(f)
        f.close()
        print(sistema)
        print("Se ha cargado exitosamente.")
    else:
        print("El archivo {} no existe.".format(nombre_archivo))
    return x

def guardarSistema(sistema):
    nombre_archivo = input("\nIngrese el nombre del archivo donde desea guardar: ")
    f = open(nombre_archivo, "wb")
    dump(sistema, f)
    f.close()
    return sistema
