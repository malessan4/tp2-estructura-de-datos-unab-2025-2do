# Dada una secuencia de caracteres, obtener dicha secuencia invertida

def invertidor_python():
    secuencia = input("Ingrese una secuencia que quiera invertir: ")
    secuencia_invertida = secuencia[::-1]
    print(secuencia)
    print(secuencia_invertida)
    


# De forma recursiva

def invertor_rec(secuencia):
    if len (secuencia) <= 1:
        return secuencia
    else:
        return secuencia[-1] + invertor_rec(secuencia[:-1])
    
def invertidor():
    secuencia = input("Ingrese una secuencia que quiera invertir: ")
    secuencia_invertida = invertor_rec(secuencia)
    
    print(f"Secuencia original: {secuencia}")
    print(f"Secuencia invertida: {secuencia_invertida}")

invertidor()
invertidor_python()