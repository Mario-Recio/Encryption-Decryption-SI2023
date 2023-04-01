import base64

mensaje = input()
base64_bytes = mensaje.encode('ascii')
mensaje_bytes = base64.b64decode(base64_bytes)
mensaje = mensaje_bytes.decode('ascii')

print(mensaje)

