
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Imprimir biografía', accion1),
        '2': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Biografía:')
    print('Nombre: Shirley Guadalupe Terrazas Paco')
    print('Edad: 19 años')
    print('Estudiante: Universitaria')
    print('Carrera: Ing. Diseño y Animacion Digital')
    print('Naci en Chuquisaca_Oropeza_Sucre bachiller del Colegio "Unidad Educativa Tecnica Humanistica Domingo Savio" curso el tercer año de universidad')
    print('realizando practica de cursos individuales, economia estable, exjugadora Olimpica de juegos basquet, ajedrez, natacion')
    print('cursado clases de ilustraitor y photoshop certificados, trabajo ilustrador individual.')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()
