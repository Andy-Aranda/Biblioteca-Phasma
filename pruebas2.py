import sistema_biblio as sb
import ejemplar as e


def crearLibros(catalogo):
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

catalogo = sb.SistemaBiblio()
crearLibros(catalogo)
crearLibros(catalogo)
print(catalogo.get_Catalogo())
#for elementos in catalogo.get_disponibles("titulo1"):
    #print(elementos)
