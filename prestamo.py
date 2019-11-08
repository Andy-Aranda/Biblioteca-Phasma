from enum import Enum
from datetime import date
from datetime import datetime
from datetime import timedelta
"""Clase Prestamo, crea objetos de tipo Prestamo cuyos atributos
son el tipo de prestamo (se elige mediante enumeración), la fecha de 
prestamo, el usuario a quien se le presta, el numero de ejemplar que
se presta."""
class TipoPrestamo(Enum):
	prestamo_regular = 1 # dos semanas
	prestamo_rapido = 2 # dos dias

class Prestamo():
	def __init__(self, tipo_prestamo, usuario, ejemplar):
		self.__tipo_prestamo = TipoPrestamo(tipo_prestamo).name
		self.__fecha_prestamo = date.today()
		if TipoPrestamo(tipo_prestamo) == 1: #por que se sumo aqui
			self.__fecha_devuelta = self.__fecha_prestamo + timedelta(weeks=2)
		else:
			self.__fecha_devuelta = self.__fecha_prestamo + timedelta(days=2)
		self.__usuario = usuario #recibe un objeto usuario??
		self.__usuario.add_libros_en_prestamo()

		self.__ejemplar = ejemplar #recibe un objeti ejemplar???
		self.__ejemplar.set_disponibilidad(False)

	def get_tipo_prestamo(self):
		"""Metodo que devuelve el tipo de prestamo."""
		return self.__tipo_prestamo

	def get_fecha_prestamo(self):
		"""Metodo que devuelve la fecha de prestamo."""
		return self.__fecha_prestamo.strftime('%d-%m-%Y')

	def get_fecha_devuelta(self):
		"""Metodo que devuelve la fecha de regreso del libro, 
		calculada con base en la fecha de prestamo y el tipo de prestamo."""
		return self.__fecha_devuelta.strftime('%d-%m-%Y')

	def get_usuario(self):
		"""Metodo que devuelve el id del usuario."""
		return self.__usuario.get_id()

	def get_libro(self):
		"""Metodo que devuelve el titulo del ejemplar prestado."""
		return self.__ejemplar.get_titulo()

	def terminar_prestamo(self):
		"""Metodo que termina el prestamo de un libro, ademas multa al usuario
		si se regreso el libro despues de tiempo."""
		usuario.dec_libros_en_prestamo()
		libro.set_disponibilidad(True)
		if self.__fecha_devuelta <= date.today():
			return False #No hay multa
		else:
			return True #SÃ­ hay multa

	def __str__(self):
		"""Metodo toString, imprime la informacion basica del prestamo."""
		return "Libro: {}, ID usuario: {} \nFecha de salida: {}\tFecha de entrega: {}".format(self.get_libro(), self.get_usuario(), self.get_fecha_prestamo(), self.get_fecha_devuelta())
