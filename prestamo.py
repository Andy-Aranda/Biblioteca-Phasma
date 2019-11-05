from enum import Enum
from datetime import date
from datetime import datetime
from datetime import timedelta

class TipoPrestamo(Enum):
	prestamo_regular = 1 # dos semanas
	prestamo_rapido = 2 # dos dias

class Prestamo():
	def __init__(self, tipo_prestamo, usuario, ejemplar):
		self.__tipo_prestamo = TipoPrestamo(tipo_prestamo).name
		self.__fecha_prestamo = date.today()
		if TipoPrestamo(tipo_prestamo) == 1:
			self.__fecha_devuelta = self.__fecha_prestamo + timedelta(weeks=2)
		else:
			self.__fecha_devuelta = self.__fecha_prestamo + timedelta(days=2)
		self.__usuario = usuario #recibe un objeto usuario??
		self.__usuario.add_libros_en_prestamo()

		self.__ejemplar = ejemplar #recibe un objeti ejemplar???
		self.__ejemplar.set_disponibilidad(False)

	def get_tipo_prestamo(self):
		return self.__tipo_prestamo

	def get_fecha_prestamo(self):
		return self.__fecha_prestamo.strftime('%d-%m-%Y')

	def get_fecha_devuelta(self):
		return self.__fecha_devuelta.strftime('%d-%m-%Y')

	def get_usuario(self):
		return self.__usuario.get_id()

	def get_libro(self):
		return self.__ejemplar.get_titulo()

	def terminar_prestamo(self):
		usuario.dec_libros_en_prestamo()
		libro.set_disponibilidad(True)
		if self.__fecha_devuelta <= date.today():
			return False #No hay multa
		else:
			return True #Sí hay multa

	def __str__(self):
		return "Libro: {}, Id usuario: {} \nFecha Salida: {}\tFecha Entrega: {}".format(self.get_libro(), self.get_usuario(), self.get_fecha_prestamo(), self.get_fecha_devuelta())
