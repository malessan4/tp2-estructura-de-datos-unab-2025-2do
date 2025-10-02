# Definir una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.

def suma_escalonada(numero):

    def calculo(numero): # Hice una funcion dentro de otra para que solo me imprima el resultado final
        if numero == 0:
            return 0
        elif numero < 0:
            return None
        else:
            return numero + calculo(numero - 1)
        
    resultado = calculo(numero)  #Puse condicionales para todas las posibilidades
    if resultado is None:
        print("Ingrese un número positivo por favor")
    elif resultado == 0:
        print("No se puede sumar 0")
    else:
        print (f"La suma de {numero} es {resultado}")
        return resultado
        


suma_escalonada(4)
suma_escalonada(0)
suma_escalonada(-1)


