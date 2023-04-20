from Crypto.Cipher import AES
def addPadding(cadena):
    while len(cadena)%16!=0:
        cadena=cadena+"\x02".encode() #se añaden espacios como padding para tener un tamaño compatible
    return cadena

cadena=input().strip().encode()


key=b"SeguridadInforma"
IV=b"SeguridadInforma"
encriptador=AES.new(key,AES.MODE_CBC,IV)

cadena=addPadding(cadena)
encoded=encriptador.encrypt(cadena) #se codifica e imprime en hexadecimal
print(encoded.hex())



