import ejemplar as e
import prestamo as p
import sistema_biblio as sb
import usuario as u
import submenus as sm

from pickle import dump, load
import os.path as path

sistema = sb.SistemaBiblio()

libro = e.Ejemplar("titulo3", "autor", "editorial", "year", True, 2,  True)
sistema.add_Libros(libro)
libro = e.Ejemplar("titulo3", "autor", "editorial", "year", False, 2,  False)
sistema.add_Libros(libro)
libro = e.Ejemplar("titulo4", "autor4", "editorial4", "year4", True, 1,  True)
sistema.add_Libros(libro)

user = u.Usuario("Tan")
sistema.add_Usuario(user)

print(sistema.buscar_en_catalogo("titulo"))

sistema = sm.cargarAlSistema(sistema)

libro = e.Ejemplar("titulo4", "autor4", "editorial4", "year4", True, 1,  True)
sistema.add_Libros(libro)

print(sistema.buscar_en_catalogo("titulo"))
