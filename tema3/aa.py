def prod(A, a, b, c, p, q, eps):
    a_prod = []
    b_prod = []
    c_prod = []

    if 0 in A[0].keys():
        aux = a[0] * A[0][0]
    else:
        aux = a[0] * 0

    if 1 in A[0].keys():
        aux1 = c[0] * A[0][1]
    else:
        aux1 = c[0] * 0

    a_prod.append(aux + aux1)

    if 0 in A[1].keys():
        aux = a[0] * A[1][0]
    else:
        aux = a[0] * 0

    if 1 in A[1].keys():
        aux1 = c[0] * A[1][1]
    else:
        aux1 = c[0] * 0

    a_prod.append(aux + aux1)

    x = 0
    for i in range(0, len(b) - 1):
        # bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        if x in A[i].keys():
            aux1 = b[x] * A[i][x]
        else:
            aux1 = b[x] * 0

        if x + 1 in A[i].keys():
            aux2 = a[x + 1] * A[i][x + 1]
        else:
            aux2 = a[x + 1] * 0

        if x + 2 in A[i].keys():
            aux3 = c[x + 1] * A[i][x + 2]
        else:
            aux3 = c[x + 1] * 0

        suma = aux1 + aux2 + aux3

        b_prod.append(suma)

        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        if x in A[i + 1].keys():
            aux1 = b[x] * A[i + 1][x]
        else:
            aux1 = b[x] * 0

        if x + 1 in A[i + 1].keys():
            aux2 = a[x + 1] * A[i + 1][x + 1]
        else:
            aux2 = a[x + 1] * 0

        if x + 2 in A[i + 1].keys():
            aux3 = c[x + 1] * A[i + 1][x + 2]
        else:
            aux3 = c[x + 1] * 0

        suma = aux1 + aux2 + aux3

        a_prod.append(suma)

        # ccccccccccccccccccccccccccccccccccccccccccccc
        if x in A[i + 3].keys():
            aux1 = b[x] * A[i + 3][x]
        else:
            aux1 = b[x] * 0

        if x + 1 in A[i + 3].keys():
            aux2 = a[x + 1] * A[i + 3][x + 1]
        else:
            aux2 = a[x + 1] * 0

        if x + 2 in A[i + 3].keys():
            aux3 = c[x + 1] * A[i + 3][x + 2]
        else:
            aux3 = c[x + 1] * 0

        suma = aux1 + aux2 + aux3

        c_prod.append(suma)

    x += 1
    i = len(b) - 1

    if x in A[i].keys():
        aux1 = b[x] * A[i][x]
    else:
        aux1 = b[x] * 0

    if x + 1 in A[i].keys():
        aux2 = a[x + 1] * A[i][x + 1]
    else:
        aux2 = a[x + 1] * 0

    suma = aux1 + aux2

    a_prod.append(suma)

    return a_prod

def prod(A, a, b, c, p, q, eps):

    AUX=[]
    AUX.insert(len(A), {})
    suma=A[0][0]*a[0]
    AUX[0].update({0: suma})

    for linie in range(1, len(A)):
        AUX.insert(len(A), {})

        suma=0
        for key in A[linie].keys():

            if key == linie - 1:
                suma += A[linie][key] * b[key]
            if key == linie:
                suma += A[linie][key] * a[key]
            if key == linie + 1:
                suma += A[linie][key] * c[key-1]
            AUX[linie].update({linie: suma})

    return AUX