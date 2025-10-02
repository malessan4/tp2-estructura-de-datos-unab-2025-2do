unab = []

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
    if unab == None:
        print("No hay alumno registrado")
        return
    for alumno in unab:
        print(f"{alumno[0]} {alumno[1]} {alumno[2]} {alumno[3]}")


imprimir_alumno()
ingresar_alumno()
imprimir_alumno()