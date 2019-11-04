from enum import Enum
from datetime import date
from datetime import timedelta

class TipoPrestamo(Enum):
	prestamo_regular = 1 # dos semanas
	prestamo_rapido = 2 # dos dias

class Prestamo():
	def __init__(self, tipo_prestamo, usuario, libros):
		self.__tipo_prestamo = TipoPrestamo(tipo_prestamo).name
		self.__fecha_prestamo = date.today()
		if TipoPrestamo(tipo_prestamo) == 1:
			self.__fecha_devuelta = self.__fecha_prestamo + timedelta(weeks=2)
		else:
			self.__fecha_devuelta = self.__fecha_prestamo + timedelta(days=2)
		self.__usuario = usuario #recibe un objeto usuario??
		usuario.add_libros_en_prestamo()

		self.__libros = libro #recibe un objeti ejemplar???
		libro.set_disponibilidad(False)

	def get_tipo_prestamo(self):
		return self.__tipo_prestamo

	def get_fecha_prestamo(self):
		return self.__fecha_prestamo

	def get_fecha_devuelta(self):
		return self.__fecha_devuelta

	def get_usuario(self):
		return usuario.get_id()

	def get_libro(self):
		return str(libro)

	def terminar_prestamo(self):
		usuario.dec_libros_en_prestamo()
		libro.set_disponibilidad(True)
		if self.__fecha_devuelta <= date.today():
			return False #No hay multa
		else:
			return True #Sí hay multa

	def __str__:
		pass
