#import ejemplar as ejem
#import usuario as user
#import prestamo as prest
from pickle import dump, load
import os.path as path
"""Clase sistema biblioteca, tiene como atributos tres listas:
en self.__catalogo guarda los objetos de tipo libro, en self.__usuario 
los objetos de tipo usuario que se creen y en self.__prestamo 
los objetos de tipo prestamo."""

class SistemaBiblio():
	def __init__(self):
		self.__catalogo = []
		self.__usuarios = []
		self.__prestamos = []


	def add_Libros(self, libro):
		"""Metodo que agrega objetos de tipo libro 
		a self.__catalogo"""
		self.__catalogo.append(libro)
		return True

	def add_Usuario(self, usuario):
		"""Metodo que agrega objetos de tipo usuario
		a self.__usuarios"""
		self.__usuarios.append(usuario)
		return True

	def agregar_prestamo(self, prestamo):
		"""Metodo que agrega objetos de tipo prestamo
		a self.__prestamos"""
		self.__prestamos.append(prestamo)
		return True

	def del_libro(self, prestamo):
		"""Metodo que elimina un objeto de tipo
		libro del catalogo. Ademas regresa un valor
		True si hubo multa, de lo contrario regresa un False"""
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
		"""Metodo que regresa el catalogo."""
		return self.__catalogo

	def get_usuarios(self):
		"""Metodo que regresa la lista de usuarios."""
		return self.__usuarios

	def get_prestamos(self):
		"""Metodo que regresa la lista de prestamos."""
		return self.__prestamos

	def get_ejemplares_disponibles(self, titulo):
		"""Metodo que regresa los ejemplares disponibles. Compara 
		el titulo de los libros en el catalogo con el titulo introducido por el 
		usuario y si esta disponible lo agrega a la lista que mostrara las
		coincidencias al usuario."""
		
		lista = []
		for libros in self.__catalogo:
			if libros.get_titulo() == titulo and libros.get_disponibilidad():
				lista.append(libros)
		return lista

	def buscar_en_catalogo(self, titulo):
		"""?????"""
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
