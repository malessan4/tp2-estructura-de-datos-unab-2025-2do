unab = [{'legajo': 1635, 'nombre': 'Matias', 'apellido': 'Alessandrello', 'contrasena': 'chimango'},
        {'legajo': 3124, 'nombre': 'Jacbhoson', 'apellido': 'Fraud', 'contrasena': 'lol'},
        {'legajo': 634, 'nombre': 'Carlos', 'apellido': 'Perez', 'contrasena': 'chi'},
        {'legajo': 16, 'nombre': 'Sonia', 'apellido': 'Perez', 'contrasena': 'hola'},
        {'legajo': 15353, 'nombre': 'Nelson', 'apellido': 'Locke', 'contrasena': 'mundo'},
        {'legajo': 24463, 'nombre': 'Cristo', 'apellido': 'Gutierrez', 'contrasena': 'chicago'}]

def ingresar_alumno():
    print("****Bienvenido al programa de ingreso de alumnos de la UNAB****")
    legajo = int(input("Ingrese el numero de legajo, ingrese 0 para salir: "))
    print("****Saliendo del programa****")
    while legajo != 0:
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        contrasena = input("Ingrese la contrasena del alumno: ")
        alumno = {'legajo': legajo, 'nombre': nombre, 'apellido': apellido, 'contrasena': contrasena}
        unab.append(alumno)
        legajo = int(input("Ingrese el numero de legajo, ingrese 0 para salir: "))
    return unab

def imprimir_alumno():
    print("***Accediendo a la Base de Datos UNAB****")
    if not unab:
        print("ERROR: No hay alumno registrado")
        return
    for alumno in unab:
        print(f"Legajo: {alumno['legajo']}\nNombre: {alumno['nombre']}\nApellido: {alumno['apellido']}\nContraseña: {alumno['contrasena']}")

def legajo_menor(lista_alumnos):
    alumnos_ordenados = sorted(lista_alumnos, key=lambda x: x['legajo'])
    print("***Alumnos ordenados por legajo***")
    for alumno in alumnos_ordenados:
        print(f"Legajo: {alumno['legajo']}\nNombre: {alumno['nombre']}\nApellido: {alumno['apellido']}\nContraseña: {alumno['contrasena']}")

def nombre_mas_largo(lista_alumnos):
    nombre_largo = max(lista_alumnos, key=lambda x: len(x['nombre']))
    print("***El nombre mas largo es: ")
    print(f"Legajo: {nombre_largo['legajo']}")
    print(f"Nombre: {nombre_largo['nombre']}")
    print(f"Apellido: {nombre_largo['apellido']}")
    print(f"Contraseña: {nombre_largo['contrasena']}")


imprimir_alumno()
print()
legajo_menor(unab)
nombre_mas_largo(unab)