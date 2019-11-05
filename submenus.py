import ejemplar as e
import prestamo as p
import sistema_biblio as sb
import usuario as u

def crearLibros(catalogo):
    print("\tAgregar libros al catálogo: ")
    aumentar = True
    reiniciar = True

    titulo = input("Ingrese Titulo: ")
    autor = input("Ingrese autor: ")
    editorial = input("Ingrese editorial: ")
    year = input("Ingrese año: ")

    ejemplares = int(input("Ingrese numero de ejemplares: "))
    miLibro = e.Ejemplar(titulo, autor, editorial, year, aumentar, ejemplares, reiniciar)
    catalogo.add_Libros(miLibro)
    #print(miLibro)
    ejemplares = ejemplares - 1
    if ejemplares >= 1: #si hay más ejemplares entonces
        aumentar = False #Contador de Libro
        reiniciar = False #Reeiniciar contador de Ejemplar
        while ejemplares > 0: #crear el resto de los ejemplares
            miLibro = e.Ejemplar(titulo, autor, editorial, year, aumentar, ejemplares, reiniciar)
            catalogo.add_Libros(miLibro)
            #print(miLibro)
            ejemplares = ejemplares - 1

def crearUsuario(usuarios):
    print("\Agregar un nuevo usuario: ")
    nombre = input("Ingrese su nombre: ")
    user = u.Usuario(nombre)
    sb.add_Usuario(user)
    print("¡Nuevo usuario agregado con exito!")

def verCatalogo(catalogo):
    print("\tEl Catalogo se muestra a continuación: ")
    print(catalogo.buscar_en_catalogo())

def buscarEnCatalogo(catalogo):
    titulo = input("Ingrese el titulo que desea buscar: ")
    print("\tSu busqueda coincide con: ")
    print(catalogo.buscar_en_catalogo(titulo))

def solicitarPrestamo(catalogo, usuario):
    id = input("Ingrese el id del libro que desea solicitar: ")
    ejemplar = obtenerEjemplarPorID(catalogo, id)
    if ejemplar.get_disponibilidad():
        tipo_prestamo = escogerTipoPrestamo()
        prestamo = p.Prestamo(tipo_prestamo, usuario, ejemplar)
        catalogo.agregar_prestamo(prestamo)
        print("\n" + str(prestamo))
    else:
        print("Lo sentimos es ejemplar no está disponble")

def obtenerEjemplarPorID(catalogo, id):
    ejemplar = ""
    for libros in catalogo.get_catalogo():
        x = "{}.{}".format(libros.get_id_libro(), libros.get_id())
        if id == x:
            ejemplar = libros
    return ejemplar


def escogerTipoPrestamo():
    tipo_prestamo = int(input("Tipo de prestamo: \n 1. Prestamo Regular: dos semanas\n 2. Prestamo Rapido: dos dias\nEscoja el numero del tipo de prestamo que desea: "))
    return tipo_prestamo
