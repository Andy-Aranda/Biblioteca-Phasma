import ejemplar as e

x = 2

while x != 1:
    titulo = input("Ingrese Titulo: ")
    autor = input("Ingrese autor: ")
    editorial = input("Ingrese editorial: ")
    year = input("Ingrese año: ")

    ejemplares = int(input("Ingrese numero de ejemplares: "))
    aumentar = True
    reiniciar = True
    miLibro = e.Ejemplar(titulo, autor, editorial, year, aumentar, reiniciar)
    print(miLibro)
    ejemplares = ejemplares - 1
    if ejemplares >= 1: #si hay más ejemplares entonces
        aumentar = False #Contador de Libro
        reiniciar = False #Contador de Ejemplar
        while ejemplares > 0: #crear el resto de los ejemplares
            miLibro = e.Ejemplar(titulo, autor, editorial, year, aumentar, reiniciar)
            print(miLibro)
            ejemplares = ejemplares - 1
    x = input("ponga 1 para salir")
