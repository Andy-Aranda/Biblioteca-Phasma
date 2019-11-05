
class Usuario():
	__cuenta = 0
	def __init__(self, nombre):
		self.__nombre = nombre
		Usuario.__cuenta = Usuario.__cuenta + 1 #Aumenta cuando se a�ade un usuario
		self.__id_user = Usuario.__cuenta # id unico!
		self.__libros_en_prestamo = 0

	def get_nombre(self):
		return self.__nombre

	def get_id(self):
		return self.__id_user

	def get_libros_en_prestamo(self):
		return self.__libros_en_prestamo

	def add_libros_en_prestamo(self):
		self.__libros_en_prestamo += 1
		return self.__libros_en_prestamo

	def dec__libros_en_prestamo(self):
		self.__libros_en_prestamo -= 1
		return self.__libros_en_prestamo
