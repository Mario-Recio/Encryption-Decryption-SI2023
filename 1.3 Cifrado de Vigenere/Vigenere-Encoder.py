from enum import Enum

cadena = str(input().strip())


class Values(Enum): #enumerado de traducción
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7
    i = 8
    j = 9
    k = 10
    l = 11
    m = 12
    n = 13
    o = 14
    p = 15
    q = 16
    r = 17
    s = 18
    t = 19
    u = 20
    v = 21
    w = 22
    x = 23
    y = 24
    z = 25
    A = 26
    B = 27
    C = 28
    D = 29
    E = 30
    F = 31
    G = 32
    H = 33
    I = 34
    J = 35
    K = 36
    L = 37
    M = 38
    N = 39
    O = 40
    P = 41
    Q = 42
    R = 43
    S = 44
    T = 45
    U = 46
    V = 47
    W = 48
    X = 49
    Y = 50
    Z = 51


matrix = []
for n in range(52):
    matrix.append([])
count = 0
offset1 = 0#desplazamiento de minúsculas
offset2=0 #desplazamiento de mayúsculas
Trigger = False
mPendientes = list()
MPendientes = list()
j = 97  # valor ascii de 'a'

for i in range(52): #generar matriz de Vigenere con alfabteto de mayúsculas y minúsculas
    for j in range(97 + offset1, 123):  # poner minusculas
        matrix[i].append(chr(j))
    for indx in range(97, 97 + offset1): #las minusculas que no se hayan puesto, se guardan para hacerlo después
        mPendientes.append(chr(indx))

    for z in range(65 + offset2, 91):  # poner mayusculas'
        matrix[i].append(chr(z))
    for indx in range(65, 65 + offset2): #las mayúsculas que no se hayan puesto, se guardan para hacerlo después
        MPendientes.append(chr(indx))

    for minuscula in mPendientes:
        matrix[i].append(minuscula)
                                        # se ponen las minúsculas y mayúsculas restantes
    for mayuscula in MPendientes:
        matrix[i].append(mayuscula)

    mPendientes.clear()
    MPendientes.clear()
    if offset1 < 26:
        offset1 += 1  # la siguiente fila empieza en 'b'
    elif offset1 == 26 and Trigger == True:
        offset2 += 1  # la siguiente fila empieza en 'b'

    if Trigger == False and offset1 == 26:
        Trigger = True

encoded = ''
key = "Vigenere"
expandedKey = ""
klen = len(key)
count = 0
i = 0
encontrado = False

while len(expandedKey) < len(cadena):
    expandedKey = expandedKey + key[count]
    count += 1
    if count == len(key):
        count = 0

count = 0
for keyChar in expandedKey:
    file = Values[keyChar].value
    row = Values[cadena[count]].value
    encodedChar=matrix[file][row]               #se añade al mensaje cifrado, la letra correspondiente en la matriz
    encoded = str(encoded + str(encodedChar))
    count+=1

print(encoded)
