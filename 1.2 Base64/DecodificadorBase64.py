import base64

print("Inserte su mensaje:")
mensaje = input()

#Convertimos el mensaje a bytes
base64_bytes = mensaje.encode('ascii')

#Descodificamos el mensaje en base64
mensaje_bytes = base64.b64decode(base64_bytes)

#Lo decodificamos a caracteres ASCII para poder leerlo
mensaje = mensaje_bytes.decode('ascii')

print("El mensaje descodificado es:")
print(mensaje)

