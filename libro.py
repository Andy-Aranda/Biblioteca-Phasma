class Libro():
    __cuenta = 0
    __totales = 0
    def __init__(self, titulo, autor, editorial, year, aumentar, totales):
        #self.__num_ejemplar = int(num_ejemplares)
        if aumentar == True:
            Libro.__cuenta = Libro.__cuenta + 1 #Aumenta cuando se crea un libro
            Libro.__totales = totales
        self.__total = Libro.__totales
        self.__id_libro = Libro.__cuenta # id unico!
        self.__titulo = titulo.title()
        self.__autor = autor
        self.__editorial = editorial
        self.__year = year
        #Libro.__cuenta = Libro.__cuenta + 1 #Aumenta cuando se crea un libro


    def get_titulo(self):
        """Metodo que regresa el titulo del libro."""
        return self.__titulo

    def get_autor(self):
        """Metodo que regresa el nombre del autor."""
        return self.__autor

    def get_editorial(self):
        """Metodo que regresa la editorial del libro."""
        return self.__editorial

    def get_year(self):
        """Metodo que regresa el año del libro."""
        return self.__year

    def get_id_libro(self):
        """Metodo que regresa el id de libro."""
        return str(self.__id_libro)

    def get_total(self):
        """Metodo que regresa el total de ejemplares que hay."""
        return self.__total

    def set_cuenta(n):
        """Metodo que asigna el valor del atributo de clase cuenta."""
        Libro.__cuenta = n
        return True

    def __str__(self):
        """Metodo To String """
        return "Titulo: {}, Autor: {}, Editorial: {}, Año: {}, id: {}".format( self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_year(), self.get_id() )
