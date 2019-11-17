from libro import Libro
class Ejemplar(Libro):
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
		return self.__id_ejemplar

	def get_disponibilidad(self):
		return self.__disponible

	def set_disponibilidad(self, booleano):
		self.__disponible = booleano
		return self.__disponible

	def __str__(self):
		return "Titulo: {}, Autor: {}, Editorial: {}, Año: {}, id: {}.{} Disponible: {}".format( self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_year(), self.get_id_libro(), self.get_id(), self.get_disponibilidad())
