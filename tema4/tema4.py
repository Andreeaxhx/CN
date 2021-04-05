import math
import numpy as np


def memorare_matrice_a(file_a, file_f):
    f = open(file_a, 'r')
    lines = f.readlines()

    n = int(lines[0])
    p = int(lines[1])
    q = int(lines[2])

    a = []
    b = []
    c = []
    for line in range(4, n + 4):
        a.append(float(lines[line]))
    if 0 in a:
        print("VECTORUL a ARE UN ELEMENTE NULE!")

    for line in range(n + 5, 2 * n + 5 - p):
        c.append(float(lines[line]))

    for line in range(2 * n + 5, 3 * n + 5 - q):
        b.append(float(lines[line]))

    f = open(file_f, 'r')
    lines = f.readlines()
    f = []
    for line in range(2, len(lines)):
        f.append(float(lines[line]))
    return a, b, c, f, p, q


def gauss_seidel(a, b, c, f, epsilon):
    k = 0
    dist = 100
    x = [0] * len(f)  # [0, 0, 0, 0, 0, 0]
    while epsilon <= dist <= 10 ** 8 and k <= 10000:

        dist = 0

        aux = (f[0] - b[0] * x[1]) / a[0]
        dist += math.fabs(math.fabs(aux) - math.fabs(x[0]))
        x[0] = aux

        for i in range(1, len(f) - 1):
            aux = (f[i] - (c[i - 1] * x[i - 1]) - (b[i] * x[i + 1])) / a[i]
            dist += math.fabs(math.fabs(aux) - math.fabs(x[i]))
            x[i] = aux

        aux = (f[-1] - c[-1] * x[-2]) / a[-1]
        dist += math.fabs(math.fabs(aux) - math.fabs(x[-1]))
        x[-1] = aux

        """suma1=0
        for i in xp:
            suma1+=math.fabs(i)

        suma2=0
        for i in x:
            suma2+=math.fabs(i)"""

        # distance = math.fabs(sum(xp)-sum(x))
        # distance = math.fabs(suma1-suma2)
        # distance = np.linalg.norm(np.array(xp) - np.array(x))

        print("interatia: ", k, " - ||x_c - x_p||: ", dist)

        k += 1

    if dist < epsilon:
        print("solutia: ")
        for i in x:
            print(round(i, 4), end=" ")
            #print(i, end=" ")
    else:
        print("divergență")

    return x


def norma(a, b, c, x, f):

    prod = [a[0] * x[0] + b[0] * x[1]]
    for i in range(1, len(a) - 1):
        prod.append(c[i - 1] * x[i - 1] + a[i] * x[i] + b[i] * x[i + 1])
    prod.append(c[-1] * x[-2] + a[-1] * x[-1])

    distance = np.linalg.norm(np.array(prod) - np.array(f))

    dist = 0
    for i in range(len(prod)):
        dist += math.fabs(math.fabs(prod[i]) - math.fabs(f[i]))

    return distance, dist


a, b, c, f, p, q = memorare_matrice_a("a2", "f2")
epsilon = 10 ** -p

x = gauss_seidel(a, b, c, f, epsilon)
distance, dist = norma(a, b, c, x, f)
print("\n(norma calculata cu librarie) ||Ax - f||: ", distance)
print("(norma folosind diferenta)    ||Ax - f||: ", dist)
# print("", (6-2.5*2)/102.5, "", (7-3.5*0.00975609756097561-1.05*3)/104.88, "", (8-1.3*0.03638304403639002-0.33*4)/100, "", (9-0.73*0.06632702042752693)/101.3, "", (1-1.5*0.08836704121508297)/102.23)
