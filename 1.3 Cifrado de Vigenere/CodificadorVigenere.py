print("Inserte su mensaje:")
mensaje = list(input())
print("Inserte la clave:")
clave = list(input())

alfabeto_mayusculas = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alfabeto = ("abcdefghijklmnopqrstuvwxyz")

longitud_alfabeto = len(alfabeto)

texto_cifrado = ""
indice_clave = 0
for caracter in mensaje:

    #Miramos si el caracter del mensaje esta en mayuscula o en minuscula
    alfabetoMensaje = alfabeto
    if caracter.isupper():
        alfabetoMensaje = alfabeto_mayusculas

    # Miramos si el caracter de la clave esta en mayuscula o en minuscula
    alfabetoClave = alfabeto
    if clave[indice_clave].isupper():
        alfabetoClave = alfabeto_mayusculas

    #Buscamos las dos posiciones correspondientes en los alfabetos y las sumamos
    #Para evitar que la posición pueda apuntar a algo fuera del alfabeto hacemos el módulo
    posicion = (alfabetoMensaje.find(caracter) + alfabetoClave.find(clave[indice_clave])) % longitud_alfabeto

    texto_cifrado += alfabetoMensaje[posicion]
    indice_clave += 1

    #Se comprueba que el índice no sea más grande que el tamaño de la clave
    #En caso de que sea más grande se hace que el índice vuelva a apuntar a la primera posición.
    if indice_clave == len(clave):
        indice_clave = 0

print("El mensaje codificado es:")
print(texto_cifrado)