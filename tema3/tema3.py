import math

def inmultire_3_elem(A, line, column, a, b, c):
    suma = A[line][column] * a[column]

    if column-1 in A[line].keys():
        suma+=A[line][column-1]*b[column-1]
    if column+1 in A[line].keys():
        suma+=A[line][column+1]*c[column]

    return suma

def memorare_matrice_a(file):
    f = open(file, 'r')
    lines = f.readlines()

    n = int(lines[0])

    A=[]
    for line in range(2, len(lines)):
        val_lin_col=[float(i) for i in lines[line].split(", ")]
        valoare=val_lin_col[0]
        linie=int(val_lin_col[1])
        coloana=int(val_lin_col[2])
        A.insert(len(A), {})
        if coloana in A[linie].keys():
            A[linie].update({coloana:valoare+A[linie][coloana]})
        A[linie].update({coloana: valoare})

    aux=[i for i in A if len(i)!=0]
    return aux

def memorare_matrice_b():
    f = open('b', 'r')
    lines = f.readlines()

    n=int(lines[0])
    p=int(lines[1])
    q=int(lines[2])

    a=[]; b=[]; c=[];
    for line in range(4, n+4):
        a.append(float(lines[line]))

    for line in range(n+5, 2*n+5-p):
        b.append(float(lines[line]))

    for line in range(2*n+5, 3*n+5-q):
        c.append(float(lines[line]))

    return a, b, c, p, q

def sum(A, a, b, c, p, q, eps):
    ok=0
    for i in range(0, len(A)):
        for key in A[i]:
            if i==key:
                A[i][key] += a[key]
            elif key-i==q:
                A[i][key] += b[key-1]
            elif i-key==p:
                A[i][key] += c[key]

    AUX=memorare_matrice_a("a_plus_b")
    for i in range(0, len(A)):
        for key in A[i]:
                #print("A+B vs A+B (file): ", A[i][key], AUX[i][key])
                if math.fabs(A[i][key]-AUX[i][key])>=eps:
                    print("diferenta in modul e mai mare decat epsilon")
                    print(i, ":", key, "---", A[i][key])
                    print(i, ":", key, "---", AUX[i][key])
                    ok=1
    if ok==0:
        print("e ok")

    """for i in A:
        print(i)"""


def prod(A, a, b, c, p, q, eps):
    ok=0
    PROD=[]
    in_plus=0
    for line in range(0, len(A)):
        for column in A[line].keys():
            PROD.insert(len(PROD), {})

            if column-1>=0:
                if column-p in A[line].keys():
                    in_plus+=A[line][column-p]*a[column]
                if column-p-q in A[line].keys():
                    in_plus+=A[line][column-p-q]*b[column-2]

                PROD[line][column - 1] = c[column - 1] * A[line][column] + in_plus
                in_plus=0

            if column-p in A[line].keys():
                in_plus += A[line][column-1] * b[column-1]
            if column+q in A[line].keys():
                in_plus += A[line][column+1] * c[column]

            PROD[line][column] = a[column] * A[line][column] + in_plus
            in_plus=0

            if column<len(b):

                if column+p in A[line].keys():
                    in_plus+=A[line][column+1]*a[column+1]
                if column+p+q in A[line].keys():
                    in_plus+=A[line][column+2]*c[column+1]
                PROD[line][column+1] = b[column] * A[line][column] + in_plus
                in_plus=0

    PROD = [i for i in PROD if len(i) != 0]
    A_ori_B = memorare_matrice_a('a_ori_b')

    if len(PROD)!=len(A_ori_B):
        print("ceva nu e in regula")

    for line in range(0, len(A_ori_B)):
        if len(A_ori_B[line])!=len(PROD[line]):
            print("altceva nu e in regula")
            #print(line, "---", A_ori_B[line])
            #print(line, "---", PROD[line])

        for key in A_ori_B[line].keys():
            if math.fabs(A_ori_B[line][key]-PROD[line][key])>eps:
                print(line, key, "---A_ori_B---", A_ori_B[line][key])
                print(line, key, "-----PROD----", PROD[line][key], end="\n\n")
                ok=1
    if ok==0:
        print("e ok si aici")
    return PROD


eps=10**-7

a, b, c, p, q=memorare_matrice_b()
A=memorare_matrice_a('a')


"""print("a-----", a[513])
print("b-----", b[491])
print("c-----", c[512])"""


#print("matricea A: ")
"""for i in A:
    print(i)"""
AA=memorare_matrice_a('a')
sum(A, a, b, c, p, q, eps)
pr=prod(AA, a, b, c, p, q, eps)

"""for i in pr:
    print(i)
"""



