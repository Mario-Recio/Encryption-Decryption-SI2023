from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
def addPadding(cadena):
    while len(cadena)%16!=0:
        cadena=pad(cadena,16) #se añaden espacios como padding para tener un tamaño compatible
    return cadena

hexCode=input().strip()
key=b"SeguridadInforma"
IV=b"SeguridadInforma"

cadena=bytes.fromhex(hexCode) #pasar cadena hexadecimal a byte, para añadir el padding y llamar a la función
cadena=addPadding(cadena)

desencriptador=AES.new(key,AES.MODE_CBC,IV)
decodedByte=desencriptador.decrypt(cadena) #desencriptar la cadena

decodedByte=unpad(decodedByte,16) #eliminar padding de la cadena
decodedString=decodedByte.decode("utf-8") #cambiar formato de la solución e imprimirla
print(decodedString)

