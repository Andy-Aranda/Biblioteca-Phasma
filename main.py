import ejemplar as e
import prestamo as p
import sistema_biblio as sb
import usuario as u

import submenus as m


cat = sb.SistemaBiblio()
libro = e.Ejemplar("titulo", "autor", "editorial", "year", True, 2,  True)
cat.add_Libros(libro)
libro2 = e.Ejemplar("titulo", "autor", "editorial", "year", False, 2,  False)
cat.add_Libros(libro2)

user = u.Usuario("tani")
cat.add_Usuario(user)

prestamo = p.Prestamo(1, user, libro)
print( "disponble ", libro.get_disponibilidad())
cat.agregar_prestamo(prestamo)
print(prestamo)

print(cat.buscar_en_catalogo() + "\n")
lista = cat.get_ejemplares_disponibles("titulo")
for elementos in lista:
    print(elementos)

m.verCatalogo(cat)
m.solicitarPrestamo(cat, user)
