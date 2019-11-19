import sistema_biblio as sistema
import usuario as usuario
import submenus as sub
import prestamo as pres
import libro as libro
import ejemplar as ejemplar
from pickle import dump, load

def main():
	sb = sistema.SistemaBiblio()

	#Creamos usuarios
	user1 = usuario.Usuario("Patricio Aranda") #1
	user2 = usuario.Usuario("Maribel Zuniga") #2
	user3 = usuario.Usuario("Nadia Rodriguez") #3
	user4 = usuario.Usuario("Ermit Nutriales") #4

	#Agegamos usuarios al sistema
	sb.add_Usuario(user1)
	sb.add_Usuario(user2)
	sb.add_Usuario(user3)
	sb.add_Usuario(user4)

	#Creamos libros
	libro1 = ejemplar.Ejemplar("Ensayo sobre la ceguera", "Jose Saramago", "Alfaguara", 2005, True, 1, True )
	libro2 = ejemplar.Ejemplar("Ladrona de libros", "Markus Zusak", "Debolsillo", 2011, True, 1, True)
	libro3 = ejemplar.Ejemplar("El perfume", "Patrick Suskind", "Caminante", 1998, True, 2, True)
	libro31 = ejemplar.Ejemplar("El perfume", "Patrick Suskind", "Caminante", 1998, False, 1, False)
	libro4 = ejemplar.Ejemplar("Huesos de lagartija", "Federico Navarrete", "SM", 2008, True, 1, True)
	libro5 = ejemplar.Ejemplar("El amor en los tiempos del colera", "Gabriel Garcia Marquez", "Diana", 2015, True, 1, True)

	#Agregamos Libros al sistema
	sb.add_Libros(libro1)
	sb.add_Libros(libro2)
	sb.add_Libros(libro3)
	sb.add_Libros(libro31)
	sb.add_Libros(libro4)
	sb.add_Libros(libro5)

	#Mostrar usuarios del sistema
	for usuarios in sb.get_usuarios():
		print("\n",usuarios)

	#Creamos un prestamo
	prestamo = pres.Prestamo(1, user4, libro31)
	#Agregamos el prestamo al sistema
	sb.agregar_prestamo(prestamo)
	print("\nDespues de hacer un prestamo: \n", user4)
	print("\n", prestamo)

	#Mostramos los libros
	for libros in sb.get_catalogo():
		print("\n",libros)

	#Guardamos sistema de video en pruebas.out
	nombre_archivo = input("\nIngrese el nombre del archivo donde desea guardar: ")
	f = open(nombre_archivo, "wb")
	dump(sb, f)
	f.close()

main()
