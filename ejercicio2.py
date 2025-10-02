# Implementar una función que me permita ver si un número es capicúa o no.


def detector_capicua(numero):
    numero_a_evaluar = str(numero)
    
    if len(numero_a_evaluar) <= 1:
        return True
    elif numero_a_evaluar[0] != numero_a_evaluar[-1]:
        return False
    else:
        siguiente = numero_a_evaluar[1:-1]
        return detector_capicua(siguiente)
    


print(detector_capicua(21212)) 