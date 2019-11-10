"""Clase Usuario, crea objetos de tipo Usuario
que tiene como atributos un nombre, un id unico, 
la cantidad de libros en prestamo y ademas lleva la cuenta
que tiene como atributos un nombre, un id unico,
la cantidad de libros en prestamo y ademas lleva la cuenta
de cuantos usuarios hay registrados hasta el momento."""

class Usuario():

	__cuenta = 0
	def __init__(self, nombre):
		self.__nombre = nombre
		Usuario.__cuenta = Usuario.__cuenta + 1 #Aumenta cuando se a�ade un usuario
		self.__id_user = Usuario.__cuenta # id unico!
		self.__libros_en_prestamo = 0

	def get_nombre(self):
		"""Metodo que devuelve el nombre del usuario"""

		return self.__nombre

	def get_id(self):
		"""Metodo que devuelve el id unico del usuario"""

		return self.__id_user

	def get_libros_en_prestamo(self):
		"""Metodo que devuelve la cantidad de
		libros en prestamo"""

		return self.__libros_en_prestamo

	def add_libros_en_prestamo(self):

		"""Metodo que suma un uno a la cantidad de libros
		en prestamo del usuario cada que al 
		usuario se le presta un libro"""

		self.__libros_en_prestamo += 1
		return self.__libros_en_prestamo

	def dec__libros_en_prestamo(self):
		"""Metodo que decrementa en uno la cantidad de libros
		en prestamo cada que el usuario devuelve un libro"""

		self.__libros_en_prestamo -= 1
		return self.__libros_en_prestamo
