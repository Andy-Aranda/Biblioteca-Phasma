
class Usuario():
	__cuenta = 0
	def __init__(self, nombre):
		self.__nombre = nombre
		Usuario.__cuenta = Usuario.__cuenta + 1 #Aumenta cuando se añade un usuario
		self.__id_user = Usuario.__cuenta # id unico!



	def get_nombre(self):
		return self.__nombre

	def get_id(self):
		return str(self.__id_user)
