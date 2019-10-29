
class Ejemplar(Libro):
	__cuenta = 0 #recordar poner la condicion de si hay varios libros aumentar ejemplar (en libro)
	def __init__(self, disponible):
		Ejemplar.__cuenta = Ejemplar.__cuenta + 1 #Aumenta cuando se crea un libro
		self.__id_unico = Ejemplar.__cuenta # id unico!
		self.__disponible = disponible 
		
	
	def get_id(self):
		return str(self.__id_unico)
	
	def get_disponibles(self):
		return self.__disponibles

	"""def get_total():
		return self.__year"""

	
	"""def solicitar_prestamo():
		returnself.__solicitar_prestamo"""