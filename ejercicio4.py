# Definir una función recursiva que imprime los números sucesivos desde n hasta 10.

def funcion_sucesivo(numero):
    if numero == 10:
        return 0
    else:
        print(numero)
        return(funcion_sucesivo(numero + 1))
        
    
funcion_sucesivo(1)