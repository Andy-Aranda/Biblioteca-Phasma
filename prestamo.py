from enum import Enum
class TipoPrestamo(Enum):
	prestamo_regular = 1
	prestamo_rapido = 2
	
class Prestamo():
	def __init__(self, tipo_prestamo, fecha_prestamo, fecha_devuelta, usuario, libros):
		self.__tipo_prestamo = TipoPrestamo(tipo_prestamo).name
		#self.__fecha_prestamo = fecha_prestamo
		#self.__fecha_devuelta = fecha_devuelta
		#self.__usuario recibe un objeto usuario??
		#self.__libros recibe un objeti ejemplar???
		
	def get_tipo_prestamo(self):
		return self.__tipo_prestamo
		
	