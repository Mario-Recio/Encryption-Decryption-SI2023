print("Inserte su mensaje:")
mensaje = list(input())
print("Inserte el desplazamiento:")
desplazamiento = int(input())


alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
longitud_alfabeto = len(alfabeto)

texto_cifrado = ""
for caracter in mensaje:

    valor_caracter = ord(caracter)
    alfabeto_a_usar = alfabeto
    limite = 97
    if caracter.isupper():
        limite = 65
        alfabeto_a_usar = alfabeto_mayusculas

    posicion = (valor_caracter - limite - desplazamiento) % longitud_alfabeto
    texto_cifrado += alfabeto_a_usar[posicion]

print("El mensaje descodificado es:")
print(texto_cifrado)


