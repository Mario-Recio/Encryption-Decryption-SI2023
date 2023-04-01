cadena=str(input().strip())
key="XOR"
count=0
decode=""
expandedKey=""
cadValue=-1
keyValue=-1

while len(expandedKey)<len(cadena): #expandir clave al tamaño del mensaje
    expandedKey=expandedKey+key[count]
    count+=1
    if count==3:
        count=0

for i in range(len(cadena)):
    cadValue=ord(cadena[i]) #se pasa cada letra, de una en una, a valor ascii
    keyValue=ord(expandedKey[i]) #se pasa cada letra, de una en una, a valor ascii
    xorValue=(cadValue^keyValue) #operación XOR con los valores ascii
    decode=decode+chr(xorValue) #devolvemos el resultado ascii a string

print(decode)