unab = [{'legajo': 1635, 'nombre': 'Matias', 'apellido': 'Alessandrello', 'contrasena': 'chimango'},
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
        alumno = [legajo, nombre, apellido, contrasena]
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



imprimir_alumno()
