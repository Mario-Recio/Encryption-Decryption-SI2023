print("Inserte su mensaje:")
mensaje = list(input())
print("Inserte la clave:")
clave = list(input())


texto_solucion = ""
indice_clave = 0

for caracter in mensaje:
    #Sacamos los valores ASCII de los caracteres del mensaje y la clave
    valormensaje = ord(caracter)
    valorclave = ord(clave[indice_clave])

    #Conseguimos el valor tras hacer el XOR del mensaje y la clave
    valor_xor = valormensaje ^ valorclave

    #Convertimos el valor conseguido a un caracter y se añadimos a texto_solucion
    texto_solucion += chr(valor_xor)

    #Añadimos una posición a nestro indice para que en el proximo ciclo del bucle
    #coja el siguiente caracter de clave
    indice_clave += 1

    #Si el mensaje es más largo que clave, entonces volvemos a repetir la clave
    if indice_clave == len(clave):
        indice_clave = 0

print("Su solución es:")
print(texto_solucion)