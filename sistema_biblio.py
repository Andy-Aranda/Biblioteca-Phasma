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
		return True
		
	
	def agregar_prestamo(self, prestamo):
		self.__prestamos.append(prestamo)
		return True
		
	
	
	def del_libro(self, prestamo):
		self.__prestamos.remove(prestamo)
		multa = prestamo.terminar_prestamo()
		return multa
	
	def get_prestamo (self, id_user):
		if id_user == "":
			return self.__prestamos
		else:
			prestamos_user = []
			for prestamos in self.__prestamos:
				if prestamos.get_usuario == id_user:
			
			
					prestamos_user.append(prestamos)
				
				
	
			
