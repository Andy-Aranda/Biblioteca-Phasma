import sistema_biblio as sb
import submenus as sm

def MenuPrincipal():
    opcion = int(input("\n\tBiblioteca Phasma\n\tMenu Principal: \n1. Crear Usuario \n2. Agregar libro \n3. Solciitar Prestamo \n4. Mostrar Catalogo \n5. Buscar por titulo \n6. Cargar Sistema \n7. Guardar Sistema\n8. Salir \nEscoja una opcion: "))
    return opcion - 1

def main():
    sistema = sb.SistemaBiblio()
    opcion = 0
    submenus = [sm.crearUsuario, sm.crearLibros, sm.solicitarPrestamo, sm.verCatalogo, sm.buscarEnCatalogo, sm.cargarAlSistema, sm.guardarSistema]

    while opcion < 9:
        print(sistema)
        opcion = MenuPrincipal()
        terminar = False
        if opcion < 7:
            while terminar == False:
                terminar = submenus[opcion](sistema)

        elif opcion == 7 or opcion == 8:
            sistema = submenus[opcion](sistema)

        else:
            opcion = 9
            print("Hasta luego :)")

main()
