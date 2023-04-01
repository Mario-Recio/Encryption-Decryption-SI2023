from Crypto.Cipher import AES
def addPadding(cadena):
    while len(cadena)%16!=0:
        cadena=cadena+"\x02".encode()
    return cadena

cadena=input().strip().encode()


key=b"SeguridadInforma"
IV=b"SeguridadInforma"
encriptador=AES.new(key,AES.MODE_CBC,IV)

cadena=addPadding(cadena)
encoded=encriptador.encrypt(cadena)
print(encoded.hex())



