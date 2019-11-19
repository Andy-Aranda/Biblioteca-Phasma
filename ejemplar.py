from libro import Libro
class Ejemplar(Libro):
	"""Clase herencia de Libro, cuenta con mas atributos
	como disponibilidad e id de ejemplar"""
	__cuenta = 0 #recordar poner la condicion de si hay varios libros aumentar ejemplar (en libro)
	def __init__(self, titulo, autor, editorial, year, aumentar, totales,  reiniciar):
		super().__init__(titulo, autor, editorial, year, aumentar, totales)
		if reiniciar == True:
			Ejemplar.__cuenta = 0
		else:
			Ejemplar.__cuenta = Ejemplar.__cuenta + 1 #Aumenta cuando se crea un libro
		self.__id_ejemplar = Ejemplar.__cuenta # id unico!
		self.__disponible = True

	def get_id(self):
		"""Devuelve el id de ejemplar"""
		return self.__id_ejemplar

	def get_disponibilidad(self):
		"""Devuelve True si el ejemplar esta disponible,
		de otro modo regresa False"""
		return self.__disponible

	def set_disponibilidad(self, booleano):
		"""Asigna un valor booleano a la disponibilidad del ejemplar"""
		self.__disponible = booleano
		return self.__disponible

	def __str__(self):
		"""Metodo ToString"""
		return "Titulo: {}, Autor: {}, Editorial: {}, Año: {}, id: {}.{} Disponible: {}".format( self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_year(), self.get_id_libro(), self.get_id(), self.get_disponibilidad())
