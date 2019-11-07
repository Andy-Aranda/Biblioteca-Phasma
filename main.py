import ejemplar as e
import prestamo as p
import sistema_biblio as sb
import usuario as u

import submenus as submenu

def MenuPrincipal():
    opcion = int(input("\n\tMenu Principal: \n1. Crear Usuario \n2. Agregar libro \n3. Solciitar Prestamo \nEscoja una opcion: "))
    return opcion

def main():
    sistema = sb.SistemaBiblio()
    opcion = 0
    a = submenu.crearUsuario
    b = submenu.crearLibros
    c = submenu.solicitarPrestamo
    lista = [0, a, b, c]
    while opcion < 6:
        opcion = MenuPrincipal()
        terminar = False
        if opcion != 6:
            while terminar == False:
                terminar = lista[opcion](sistema)
        #if opcion == 2:
            #while terminar == False:
                #terminar = submenu.crearUsuario(sistema)
        else:
            opcion = 6

main()
