
def ingresar_alumno():
    print("****Bienvenido al programa de ingreso de alumnos de la UNAB****")
    alumno = []
    legajo = int(input("Ingrese el numero de legajo, ingrese 0 para salir: "))
    print("****Saliendo del programa****")
    while legajo != 0:
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        contrasena = input("Ingrese la contrasena del alumno: ")
        li = [legajo, nombre, apellido, contrasena]
        alumno.append(li)
        legajo = int(input("Ingrese el numero de legajo, ingrese 0 para salir: "))


ingresar_alumno()