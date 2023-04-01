print("Inserte su mensaje:")
mensaje = list(input())

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
longitud_alfabeto = len(alfabeto)


for i in range(24):
    texto_cifrado = ""
    for caracter in mensaje:
        valor_caracter = ord(caracter)
        alfabeto_a_usar = alfabeto
        limite = 97
        if caracter.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_caracter - limite - 1) % longitud_alfabeto
        texto_cifrado += alfabeto_a_usar[posicion]
    print(texto_cifrado)
    mensaje = texto_cifrado



