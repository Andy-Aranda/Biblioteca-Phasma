import ejemplar as e
import prestamo as p
import sistema_biblio as sb
import usuario as u
import submenus as sm

from pickle import dump, load

sistema = sm.cargarAlSistema("try.out")

libro = e.Ejemplar("titulo4", "autor4", "editorial4", "year4", True, 1,  True)
sistema.add_Libros(libro)

print(sistema.buscar_en_catalogo(""))
