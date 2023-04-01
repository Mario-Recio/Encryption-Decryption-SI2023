import base64

mensaje = input()
mensaje_bytes = mensaje.encode('ascii')
base64_bytes = base64.b64encode(mensaje_bytes)
base64_mensaje = base64_bytes.decode('ascii')

print(base64_mensaje)

