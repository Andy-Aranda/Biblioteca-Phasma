import sistema_biblio as sb
import submenus as sm
"""Menu principal. """
def MenuPrincipal():
    opcion = int(input("\n\tBiblioteca  P h a s m a\n\nMenu  Principal: \n\n\t1. Crear Usuario \n\t2. Agregar libro \n\t3. Solicitar Prestamo \n\t4. Mostrar Catalogo \n\t5. Buscar por titulo \n\t6. Cargar Sistema \n\t7. Guardar Sistema\n\tEscriba otro numero para salir. \n\nEscoja una opcion: "))
    return opcion - 1

def main():
    biblio = sb.SistemaBiblio()
    opcion = 0
    submenus = [sm.crearUsuario, sm.crearLibros, sm.solicitarPrestamo, sm.verCatalogo, sm.buscarEnCatalogo, sm.cargarAlSistema, sm.guardarSistema]
    while opcion < 7:
        try:
            opcion = MenuPrincipal()
            terminar = False
        except ValueError as excepcion:
            print("\n\t ERROR: Favor de seleccionar unicamente un numero")
        else:
            if opcion < 5:
                while terminar == False:
                    terminar = submenus[opcion](biblio)
            elif opcion == 5 or opcion == 6:
                biblio = submenus[opcion](biblio)
            else:
                print("Hasta luego :)")

if __name__ == '__main__':
    main()
