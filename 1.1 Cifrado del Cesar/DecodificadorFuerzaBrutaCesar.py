print("Inserte su mensaje:")
mensaje = list(input())

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
longitud_alfabeto = len(alfabeto)

#Hacemos este buce para sacar todas las diferentes combinaciones que puede haber
for i in range(24):
    texto_cifrado = ""
    for caracter in mensaje:

        # Sacamos el valor de ASCII del mensaje
        valor_caracter = ord(caracter)

        # Miramos si el caracter del mensaje esta en mayuscula o en minuscula
        alfabeto_a_usar = alfabeto
        limite = 97
        if caracter.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        # Le restamos un valor para que la posición del carácter corresponda con el carácter del alfabeto y le restamos 1
        # Para evitar que la posición pueda apuntar a algo fuera del alfabeto hacemos el módulo
        posicion = (valor_caracter - limite - 1) % longitud_alfabeto
        texto_cifrado += alfabeto_a_usar[posicion]

    print(texto_cifrado)
    mensaje = texto_cifrado



