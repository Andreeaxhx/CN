import math
import scipy.linalg as scp
from functii import ex1, data_file, euclidean_norm
import numpy as np


def Rpq(cos, sin, p, q, n):
    R = []
    for i in range(0, n):
        R.insert(len(R), [])
        for j in range(0, n):
            if i == j and (i == p or i == q):
                R[i].append(cos)
            elif i == j:
                R[i].append(1)
            elif i == p and j == q:
                R[i].append(sin)
            elif i == q and j == p:
                R[i].append(-sin)
            else:
                R[i].append(0)
    print("R: ", R)
    return np.array(R)


def pq(A):
    maxim = 0
    p = 1
    q = 0
    for i in range(1, len(A)):
        for j in range(0, i):
            if math.fabs(A[i][j]) > maxim:
                maxim = math.fabs(A[i][j])
                p = i
                q = j
    return p, q


def matrice_diag(A):
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if i != j:
                if A[i][j] != 0:
                    return False
    return True


def find_theta(alpha):

    if alpha >= 0:
        t = -alpha + math.sqrt((alpha ** 2 + 1))
    else:
        t = -alpha - math.sqrt((alpha ** 2 + 1))

    # print("t1: ", t1)
    # print("t2: ", t2)
    # print("atan t1: ", round(math.atan(t1), 2))
    # print("atan t2: ", round(math.atan(t2), 2))

    # if round(math.atan(t1), 2) >= 0 and round(math.atan(t1), 2) <= round(math.pi / 4, 2):
    #     return round(math.atan(t1), 2)
    # if round(math.atan(t2), 2) >= 0 and round(math.atan(t2), 2) <= round(math.pi / 4, 2):
    #     return round(math.atan(t2), 2)
    # #return 0

    return t


def matrix_array(A, n):
    A0 = A.copy()
    print("A: ", A)
    # A = np.matrix(A)
    k = 0
    U = np.identity(n)

    p, q = pq(A)
    alpha = (A[p][p] - A[q][q]) / (2 * A[p][q])
    print("p: ", p, "q: ", q)

    t = find_theta(alpha)
    print("t: ", t)

    c = 1/math.sqrt(1+t**2)
    s = t/math.sqrt(1+t**2)

    R = Rpq(c, s, p, q, n)
    print("R: ", R)



    while math.fabs(A[p][q]) > epsilon and k < 10000: #while matrice_diag(A) == False and k < 10000:

        A = np.dot(np.dot(R, A), R.transpose())
        U = np.dot(U, R.transpose())

        for j in range(0, n):
            if j != p and j != q:
                A[p][j] = c * A[p][j] + s * A[q][j]
                A[q][j] = -s * A[j][p] + c * A[q][j]
                A[j][q] = -s * A[j][p] + c * A[q][j]
                A[j][p] = A[p][j]

            A[p][p] = A[p][p] + t * A[p][q]
            A[q][q] = A[q][q] - t * A[p][q]
            A[p][q] = 0
            A[q][p] = 0

        for i in range(0, n):
            aux = U[i][p]
            U[i][p] = c * U[i][p] + s * U[i][q]
            U[i][q] = -s * aux + c * U[i][q]

        # B = np.dot(R, A)
        # B = np.dot(A, R.transpose())

        # V = np.dot(U, R.transpose())

        p, q = pq(A)

        alpha = (A[p][p] - A[q][q]) / (2 * A[p][q])
        t = find_theta(alpha)
        print("t: ", t)

        c = 1 / math.sqrt(1 + t ** 2)
        s = t / math.sqrt(1 + t ** 2)

        R = Rpq(c, s, p, q, n)
        print("R: ", R)

        np.set_printoptions(suppress=True)
        print("A: ", A)

        k += 1

    #print("A: ", A)
    Afinal = np.dot(U.transpose(), A0, U)
    return Afinal


def matrix_array_cholesky(A, epsilon):
    distance = 1
    k = 0

    while distance > epsilon and k < 1000:
        print("iteratia -", k)
        A_aux = A.copy()
        L = ex1(A_aux, eps=10 ** -1)
        LT = np.transpose(L)

        AUX = np.array(LT).dot(np.array(L))

        distance = euclidean_norm(AUX, A)
        # print("norma A:   ", np.linalg.norm(A))
        # print("norma AUX: ", np.linalg.norm(AUX))
        # print(distance)

        A = AUX
        # print(A)
        k += 1

        print("norma: ", distance)
        print("A: \n", A)


def returnColRows(A):
    p = 0  # linie
    n = 0  # coloane

    for element in A:
        p += 1

    for element in A[0]:
        n += 1

    return p, n


def returnElemPozNeg(S, n, p):
    elem_neg = []
    elem_poz = []

    for line in S:
        for el in line:
            if el < 0:
                elem_neg.append(el)
            else:
                elem_poz.append(el)

    return elem_poz, elem_neg


def returnMinMax(S):
    minim = S[0]
    maxim = S[0]
    for element in S:
        if element > 0:
            if minim > element:
                minim = element
            if maxim < element:
                maxim = element

    return minim, maxim


def returnValSing(S):
    list = [elem for elem in S if elem > 0]
    return list


def createSI(S, p, n):
    elem_S = returnValSing(S)
    SI = []
    for i in range(len(elem_S)):  # range(len(elem_S))
        row = [0] * (n + 1)
        row[i] = 1 / elem_S[i]
        p -= 1
        SI.append(row)

    for i in range(p - n):
        SI.append([0] * (n + 1))

    return SI


# -------------------------------------------------PRIMA BULINA----------------------------------------------------------


# A = np.array([[1, math.sqrt(2), 2], [math.sqrt(2), 3, math.sqrt(2)], [2, math.sqrt(2), 1]])
A = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])

n, A = data_file()
epsilon = 10 ** -7
# Afinal = matrix_array(A, n)
# print("Afinal", Afinal)

# -------------------------------------------------BULINA A DOUA---------------------------------------------------------
# n, A = data_file()
print("A: ", A)
matrix_array_cholesky(A, epsilon)

# -------------------------------------------------ULTIMA BULINA---------------------------------------------------------

# A = np.array([[1,2], [3,4], [5,6]])
# A = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8]])
# A = np.array([[1, 0, 3], [0, 4, 2], [3, 2, 11]])
# U, S, V = np.linalg.svd(A)
# print("A: \n", A)
# print("U: \n", U)
# print("S: \n", S)
# print("V: \n", V)
#
# print()
#
# S_aux = S.copy()
# S = np.zeros((A.shape[0], A.shape[1]))
# S[:A.shape[1], :A.shape[1]] = np.diag(S_aux)
#
#
# n, p = returnColRows(A)
# elem_poz, elem_neg = returnElemPozNeg(S, n, p) # elem_poz cuprinde elemente >= 0
# rang = len(returnValSing(S_aux))
# minim, maxim = returnMinMax(S_aux)
#
# print("Valorile singulare ale matricii A:", elem_poz)
# print("Rangul matricii A:", rang)
# print("Numarul de conditionare al matricii A:", maxim / minim)
#
# print()
#
# # A = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8]])
# # U, S, V = np.linalg.svd(A)
#
# B = U.dot(S.dot(V))
# print("reconstructed: \n", B)
#
# SI = np.linalg.pinv(S)
# print("S: \n", S)
# print()
# print("SI: biblioteca\n", SI)
# print("SI: function\n", createSI(S_aux, p, n))
#
# print()
# pseudo_inverse = np.transpose(V).dot(SI.dot(np.transpose(U)))
# print("pseudo-inverse: \n", pseudo_inverse)
#
#
# # A = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8]])
# # U, S, V = np.linalg.svd(A)
#
# least_squares = np.linalg.inv(np.transpose(A).dot(A)).dot(np.transpose(A))
# print("least_squares:\n ", least_squares)
#
# print()
# print("||AI - AJ||: ", euclidean_norm(pseudo_inverse, least_squares))


#print(Rpq(90, 2, 3, 5))