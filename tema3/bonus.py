def memorare_matrice_a():
    f = open('bonus_a', 'r')
    lines = f.readlines()

    n=int(lines[0])
    p=int(lines[1])
    q=int(lines[2])

    a=[]; b=[]; c=[];
    for line in range(4, n + 4):
        a.append(float(lines[line]))

    for line in range(n + 5, 2 * n + 5 - q):
        b.append(float(lines[line]))

    for line in range(2 * n + 6 - q, 3 * n + 6 - p - q):
        c.append(float(lines[line]))


    return a, b, c, p, q, n

def memorare_matrice_b():
    f = open('bonus_b', 'r')
    lines = f.readlines()

    n=int(lines[0])
    p=int(lines[1])
    q=int(lines[2])

    a=[]; b=[]; c=[];
    for line in range(4, n + 4):
        a.append(float(lines[line]))

    for line in range(n + 5, 2 * n + 5 - q):
        b.append(float(lines[line]))

    for line in range(2 * n + 6 - q, 3 * n + 6 - p - q):
        c.append(float(lines[line]))

    return a, b, c, p, q, n


def produs(a1, b1, c1, a2, b2, c2, p1, p2, q1, q2, n):

#----------------------------------------A1*A2------------------------------------------------
    A1A2=[]
    suma=a1[0]*a2[0]
    if q1==p2:
        suma+=b1[0]*c2[0]
    A1A2.append(suma)

    for i in range(1, len(a1)):
        suma=0
        if i>=n-len(c1):
            if p1==q2:
                suma+=c1[i-p1]*b2[i-q2]
        if q1 == p2 and i<len(b1) :
            suma += b1[i] * c2[i]

        suma+=a1[i]*a2[i]
        A1A2.append(suma)

#----------------------------------------A1*B2------------------------------------------------
    A1B2 = []
    suma = a1[0] * b2[0]
    if q1 == q2:
        suma += b1[0] * a2[0+q2]
    A1B2.append(suma)
    for i in range(1, len(b2)):
        suma = 0
        suma +=a1[i] * b2[i]
        if i >= n - len(c1):
            if q1 == p2+q2:
                suma += b1[i] * c2[i + q2] #??????
        if q1 == q2:
            suma += b1[i] * a2[i+q2]

        A1B2.append(suma)


#----------------------------------------A1*C2------------------------------------------------
    A1C2 = []
    for i in range(0, len(c2)-1):
        suma = 0
        suma += a1[i+p2] * c2[i]
        if i >= n - len(b2):
            if p2+q2==p1:
                suma += c1[i+p2] * b2[i]  # ??????
        if p1 == p2:
            suma += c1[i] * a2[i]

        A1C2.append(suma)

    suma = a1[len(a1) - 1] * c2[len(c2) - 1]
    if p1 == p2:
        suma += c1[len(c1) - 1] * a2[0]
    A1C2.append(suma)


#----------------------------------------B1*A2------------------------------------------------
    # B1A2=[]
    # suma = b1[0] * a2[0 + q1]
    # if q1==q2:
    #     suma+=a1[0]*b2[0]
    # B1A2.append(suma)
    # for i in range(1, len(b1)):
    #     suma=0
    #     suma+=b1[i]*a2[i+q1]
    #     if i >= n - len(c1):
    #         if p1+q1 == q2:
    #             suma += c1[i-p1] * b2[i-p1]
    #     if q1==q2:
    #         suma += a1[i] * b2[i]
    #     B1A2.append(suma)

    B1A2 = []
    for i in range(0, len(b1)):
        suma=0
        print(b1[i])
        print(a2[i+q1])
        suma+=b1[i]*a2[i+q1]

        if q1==q2:
            suma+=a1[i]*b2[i]

        if suma!=0:
            B1A2.append(suma)

#---------------------------------------B1*B2------------------------------------------------

    B1B2=[]

    if q1 < len(b2):
        for i in range(0, len(a2)-q1-q2):  #len(a2)-q1-q2
            suma=0
            suma+=b1[i]*b2[i+q1]
            B1B2.append(suma)
        li1=1
        co1=len(a1)-(len(b2)-(len(b1)))+1  #1+q1
        #co1 = 1+q1
    else:
        li1=None
        co1=None

#---------------------------------------B1*C2------------------------------------------------

    B1C2 = []


    if q1<p2:
        for i in range(0, len(c2)): #len(b1)
            suma=0
            suma+=b1[i+len(c2)-len(b1)]*c2[i]

            if p1 == q2 and len(b1) > len(a1) - len(c1):
                suma += c1[i - p1] * b2[i - p1]

            if p1 + q1 == p2 + q2:
                suma += c1[i] * b2[i]
            if suma != 0:
                B1C2.append(suma)

    if q1 > p2:
        for i in range(0, len(b1)):
            suma = 0
            suma += b1[i] * c2[i + len(c2) - len(b1)]

            if p1 == q2 and i > len(a1) - len(c1):
                suma += c1[i - p1] * b2[i - p1]

            if p1 + q1 == p2 + q2:
                suma += c1[i] * b2[i]
            if suma != 0:
                B1C2.append(suma)

            """suma=0
            suma+=b1[i]*c2[i+q1-p2]
            if q1==p2:
                print("hei1")
                #suma+=b1[i]*c2[i]
                suma+=a1[i]*a2[i]
            if p1==q2 and len(b1)>len(a1)-len(c1):
                print("hei2")
                suma+=c1[i-p1]*b2[i-p1]
    
            if p1+q1==p2+q2:
                print("hei3")
                suma+=c1[i]*b2[i]
    
            if suma!=0:
                B1C2.append(suma)
    """
        li2=1
        co2=len(c2)-len(b1)+1   #len(a1)-q1
    else:
        li2=None
        co2=None


#----------------------------------------C1*A2------------------------------------------------
    C1A2 = []

    for i in range(0, len(c1)-1):
        suma = 0
        suma += c1[i] * a2[i]
        if i < len(c2):
            if p1 + q1 == p2:
                suma += b1[i + p1] * c2[i]
        if p1 == p2:
            suma += a1[i + p1] * c2[i]
        C1A2.append(suma)

    suma=c1[len(c1)-1]*a2[len(c1)-1]
    if p1==p2:
        suma+=a1[len(c1)+p1-1]*c2[len(c1)-1]
    C1A2.append(suma)


#---------------------------------------C1*B2------------------------------------------------
    C1B2=[]

    if(len(c1)<len(b2)):
        lungime=len(c1)
    else:
        lungime=len(b2)
    for i in range(0, lungime):
        suma=0
        suma+=c1[i]*b2[i]
        if p1==q2:
            suma+=a1[i+p1]*a2[i+q2]
        if p1+q1==q2:
            suma+=b1[i+p1]*a2[i+q2]

        if suma!=0:
            C1B2.append(suma)

        li3=1+p1
        co3=q2+1

#---------------------------------------C1*C2------------------------------------------------
    C1C2=[]
    if p1<len(c2):
        for i in range(0, len(a1)-p1-p2):
            suma=0
            suma+=c1[i+p2]*c2[i]
            C1C2.append(suma)
        li4=p1+p2+1
        co4=1
    else:
        li4=None
        co4=None









    return A1A2, A1B2, A1C2, B1A2, B1B2, (li1, co1), B1C2, (li2, co2),  C1A2, C1B2, (li3, co3), C1C2, (li4,co4)

a1, b1, c1, p1, q1, n1=memorare_matrice_a()
a2, b2, c2, p2, q2, n2=memorare_matrice_b()

A1A2, A1B2, A1C2, B1A2, B1B2, (li1, co1), B1C2, (li2, co2), C1A2, C1B2, (li3, co3), C1C2, (li4,co4) = produs(a1, b1, c1, a2, b2, c2, p1, p2, q1, q2, n1)

print("A1A2: ", A1A2)
print("A1B2: ", A1B2)
print("A1C2: ", A1C2)
print("B1A2: ", B1A2)
print("B1B2: linia", li1, "coloana", co1, "-", B1B2)
print("B1C2: linia", li2, "coloana", co2, "-", B1C2)
print("C1A2: ", C1A2)
print("C1B2: linia", li3, "coloana", co3, "-", C1B2)
print("C1C2: linia", li4, "coloana", co4, "-", C1C2)
