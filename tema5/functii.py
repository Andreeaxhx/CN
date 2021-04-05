import numpy as np
import math

def ex1(A, eps):
    if np.array_equal(A, A.transpose()) == False:
        print("Matrix not symmetric!")
    #verificam si daca e pozitiv definita??

    d=[]
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if i==j:
                d.append(A[i][j])

    for j in range(0, len(A)):
        for i in range(0, len(A[j])):
            if i==j:
                sum = 0
                for k in range(0, j):
                    sum=sum+(A[j][k]**2)
                A[j][j]=math.sqrt(d[j]-sum)
            elif i>j:
                sum = 0
                for k in range(0, j):
                    sum = sum + (A[i][k] * A[j][k])
                if math.fabs(A[j][j])>eps:
                    A[i][j] = (A[i][j] - sum)/A[j][j]
                else:
                    print("nu se poate")
            elif j>i:
                A[i][j]=0
    #print("\nL: \n", A)
    #print("\n L transpus: \n", A.transpose())
    #A = A.dot(A.transpose())
    #print("L * L transpus = A: \n", A.dot(A.transpose()))
    return A

def data_file():
    file1 = open('data', 'r')
    lines = file1.readlines()
    A=[]
    n=int(lines[0])
    l=1
    while len(A)<n:
        A.append([float(x) for x in lines[l].split(" ")])
        l+=1
    b=[float(x) for x in lines[l].split(" ")]
    A=np.array(A)
    b=np.array(b)
    eps = 10**-8

    return n, A

def euclidean_norm(A, B):

    suma1 = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            suma1 += (math.fabs(A[i][j]) - math.fabs(B[i][j])) ** 2

    # suma2 = 0
    # for i in range(0, len(B)):
    #     for j in range(0, len(B[i])):
    #         suma2 += (B[i][j]) ** 2
    #
    # suma = math.fabs(math.sqrt(suma1) - math.sqrt(suma2))
    return math.sqrt(suma1)


