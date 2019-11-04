import ejemplar as ejem
import usuario as user
import prestamo as prest

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

	def solicitar_prestamo(self, id):
		pass
