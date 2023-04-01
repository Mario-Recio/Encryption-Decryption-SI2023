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

    alfabetoMensaje = alfabeto
    if caracter.isupper():
        alfabetoMensaje = alfabeto_mayusculas

    alfabetoClave = alfabeto
    if clave[indice_clave].isupper():
        alfabetoClave = alfabeto_mayusculas

    posicion = (alfabetoMensaje.find(caracter) - alfabetoClave.find(clave[indice_clave])) % longitud_alfabeto

    texto_cifrado += alfabetoMensaje[posicion]
    indice_clave += 1

    if indice_clave == len(clave):
        indice_clave = 0

print("El mensaje descodificado es:")
print(texto_cifrado)