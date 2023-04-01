import base64

print("Inserte su mensaje:")
mensaje = input()

#Convertimos el mensaje a bytes
mensaje_bytes = mensaje.encode('ascii')

#Codificamos el mensaje en base64
base64_bytes = base64.b64encode(mensaje_bytes)

#Dcodificamos para pasar a caracteres ASCII obteniendo el mensaje codificado en base64
base64_mensaje = base64_bytes.decode('ascii')

print("El mensaje codificado es:")
print(base64_mensaje)

