import ejemplar as e
import prestamo as p
import sistema_biblio as sb
import usuario as u

import os.path as path
from pickle import dump, load

"""Define el funcionamiento de las ocpiones que se presentan al usuario en el main."""

def crearLibros(sistema):
    """Si el usuario desea agregar un libro, solicita los datos del mismo. Considera los errores que 
    el usuario pudiera cometer al ingresarlo. Ademas considera el numero de ejemplares que el usuario quiera agregar,
    si es mas de uno no aumenta el id de libro, pero si el de ejemplar, por lo que se crean varios ejemplares del mismo libro y
    se agregan a la lista de libros. De lo contrario, se agrega el unico libro mencionado."""
    
    
    print("\tAgregar libros al catálogo: ")
    aumentar = True
    reiniciar = True

    titulo = input("Ingrese Titulo: ")
    autor = input("Ingrese autor: ")
    editorial = input("Ingrese editorial: ")
    year = input("Ingrese año: ")

    error = True
    while error:
        try:
            ejemplares = int(input("Ingrese numero de ejemplares: "))
        except ValueError as excepcion:
            print("\n\t Escriba un numero valido de ejemplares: " + excepcion)
        else:
            error = False
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
        print("Se han agregado con exito los libros")
    else:
        print("Se ha agregado con exito el libro")
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
    j = 0
    lista = mostrar_de_catalogo("", sistema)
    for i in lista:
        j += 1
        print( "{}. {}\n".format(j, i[0]) )
    miniMenuShowEjemplares(lista)
    return True

def miniMenuShowEjemplares(lista):
    opcion = int(input("Escoja una opcion: \n1. Mostar ejemplares disponbles \n2. Regresar al Menu Principal \nEscoja una opcion: "))
    if opcion == 1:
        n = int(input("Ingrese el numero de los ejemplares que desea ver: "))
        ejemplares = lista[n-1][1]
        for n in ejemplares:
            print(n)

def buscarEnCatalogo(sistema):
    titulo = input("Ingrese el titulo que desea buscar: ")
    lista = mostrar_de_catalogo(titulo, sistema)
    if lista == []:
        print("\tSu busqueda no coincide con nada.")
    else:
        j = 0
        print("\tSu busqueda coincide con: ")
        for i in lista:
            j += 1
            print( "{}. {}\n".format(j, i[0]) )
    miniMenuShowEjemplares(lista)
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
            print("\nInformacion de su prestamo:\n" + str(prestamo))
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
    error = True
    while error:
        try:
            tipo_prestamo = int(input("Tipo de prestamo: \n 1. Prestamo Regular: dos semanas\n 2. Prestamo Rapido: dos dias\nEscoja el numero del tipo de prestamo que desea: "))
        except ValueError as excepcion:
            print("\n\t ERROR: Favor de seleccionar unicamente un numero de las opciones")
        else:
            if tipo_prestamo >= 3:
                print("\n\t ERROR: Favor de seleccionar unicamente un numero de las opciones\n")
            else:
                error = False
    return tipo_prestamo


def cargarAlSistema(sistema):
    x = sistema
    nombre_archivo = input("\nIngrese el nombre del archivo que desea cargar: ")
    if path.exists(nombre_archivo):
        f = open(nombre_archivo, "rb")
        x = load(f)
        f.close()
        #print(sistema)
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

def get_ejemplares_disponibles(titulo, sistema):
    lista = []
    for libros in sistema.get_catalogo():
        if libros.get_titulo() == titulo and libros.get_disponibilidad():
            lista.append(libros)
    return lista

def mostrar_de_catalogo(titulo, sistema):
    libros = []
    nombre = ""
    titulo = titulo.title() #Formato de titulo a la entrada del usuario
    if titulo == "":
        for l in  sistema.get_catalogo():
            if l.get_titulo() != nombre:
                ejemplares = get_ejemplares_disponibles( l.get_titulo(), sistema )
                libros.append( ["{} ({}/{})".format( str(l), (len(ejemplares) ), l.get_total()), ejemplares ] )
                nombre = l.get_titulo()
    else:
        for l in sistema.get_catalogo():
            if l.get_titulo() != nombre :
                ejemplares = get_ejemplares_disponibles( l.get_titulo(), sistema )
                libros.append( ["{} ({}/{})".format( str(l), (len(ejemplares) ), l.get_total()), ejemplares ] )
                nombre = l.get_titulo()

    return libros
