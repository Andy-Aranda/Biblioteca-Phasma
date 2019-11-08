#import ejemplar as ejem
#import usuario as user
#import prestamo as prest
from pickle import dump, load
import os.path as path

class SistemaBiblio():
	def __init__(self):
		self.__catalogo = []
		self.__usuarios = []
		self.__prestamos = []


	def add_Libros(self, libro):
		self.__catalogo.append(libro)
		return True

	def add_Usuario(self, usuario):
		self.__usuarios.append(usuario)
		return True

	def agregar_prestamo(self, prestamo):
		self.__prestamos.append(prestamo)
		return True

	def del_libro(self, prestamo):
		self.__prestamos.remove(prestamo)
		multa = prestamo.terminar_prestamo()
		return multa

	#def get_prestamos_by_user(self, id_user): #Obtener el prestamos de un usuario
		#if id_user == "":
			#return self.__prestamos
		#else:
			#prestamos_user = []
			#for prestamos in self.__prestamos:
				#if prestamos.get_usuario == id_user:
					#prestamos_user.append(prestamos)
			#return prestamos_user

	def get_catalogo(self):
		return self.__catalogo

	def get_usuarios(self):
		return self.__usuarios

	def get_prestamos(self):
		return self.__prestamos

	def get_ejemplares_disponibles(self, titulo):
		lista = []
		for libros in self.__catalogo:
			if libros.get_titulo() == titulo and libros.get_disponibilidad():
				lista.append(libros)
		return lista

	def buscar_en_catalogo(self, titulo):
		texto = ""
		nombre = ""
		if titulo == "":
			for libros in self.__catalogo:
				if libros.get_titulo() != nombre:
					texto = texto + "\n{} ({}/{})".format( str(libros), (len(self.get_ejemplares_disponibles(libros.get_titulo()))), libros.get_total())
					nombre = libros.get_titulo()
		else:
			for libros in self.__catalogo:
				if libros.get_titulo() != nombre :
					texto = texto + "\n{} ({}/{})".format( str(libros), (len(self.get_ejemplares_disponibles(libros.get_titulo()))), libros.get_total())
					nombre = libros.get_titulo()

		return texto
