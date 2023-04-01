print("Inserte su mensaje:")
mensaje = list(input())
print("Inserte el desplazamiento:")
desplazamiento = int(input())

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
longitud_alfabeto = len(alfabeto)

texto_cifrado = ""
for caracter in mensaje:

    #Sacamos el valor de ASCII del mensaje
    valor_caracter = ord(caracter)

    # Miramos si el caracter del mensaje esta en mayuscula o en minuscula
    alfabeto_a_usar = alfabeto
    limite = 97
    if caracter.isupper():
        limite = 65
        alfabeto_a_usar = alfabeto_mayusculas

    # Le restamos un valor para que la posición del carácter corresponda con el carácter del alfabeto y le sumamos el desplazamiento
    # Para evitar que la posición pueda apuntar a algo fuera del alfabeto hacemos el módulo
    posicion = (valor_caracter - limite + desplazamiento) % longitud_alfabeto
    texto_cifrado += alfabeto_a_usar[posicion]

print("El mensaje codificado es:")
print(texto_cifrado)