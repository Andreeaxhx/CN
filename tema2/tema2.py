import math
import numpy as np
import scipy.linalg as scp
import random

#1. Sa se calculeze descompunerea LLT (descompunerea/factorizarea Cholesky) a matricii A (A = LLT ), unde L este matrice inferior triunghiulara
#cu elementele de pe diagonala pozitive (lii > 0, ∀i)

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
    print("\nL: \n", A)
    #print("\n L transpus: \n", A.transpose())
    #A = A.dot(A.transpose())
    print("L * L transpus = A: \n", A.dot(A.transpose()))
    return A

#2. Folosind aceasta descompunere, sa se calculeze determinantul matricii A (det A = det L * det LT)

def ex2(A, eps):
    #A=ex1(A, eps)
    detA=1
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if i==j:
                detA=detA*(A[i][j]**2)
    print("\ndet A:", detA)

#3. Utilizand descompunerea Cholesky calculata mai sus si metodele substitutiei directe si inverse,
# sa se calculeze xChol, o solutie aproximativa a sistemului Ax = b

def ex3(A, eps, b):

    #substitutia directa
    y=[]
    #L=ex1(eps, A)
    L=A

    for i in range(0, len(b)):
        sum=b[i]
        for l in range(0, i):
            sum-=L[i][l]*y[l]
        y.append(sum/L[i][i])

    #substitutia inversa
    x=np.zeros(n)
    LT=L.transpose()

    for i in range(n-1, -1, -1):
        sum=y[i]
        for l in range(0, n-i):
            sum-=LT[i][i+l]*x[i+l]

        x[i]=(sum/LT[i][i])
    #x.reverse()
    print("\nsolutia sistemului ex. 3:             ", x)
    return x

#4. Sa se verifice solut¸ia calculata prin afisarea normei: ||Ainit * Xchol − b||2 (aceasta norma ar trebui sa fie mai mica decat 10−8, 10−9)
# Ainit este matricea initiala, ||·||2 este norma euclidiana.

def ex4(A, Xchol, b):

    A=np.matrix(A.dot(A.transpose()))
    prod=A*np.transpose(np.matrix(Xchol))
    prod=prod-np.transpose(np.matrix(b))

    sum=0
    for i in prod:
        for j in i:
            sum+=j**2
    sum=math.sqrt(sum)
    print("\n||A**init * Xchol − b||2: ", sum)

#5. Folosindu-se una din bibliotecile mentionate in pagina laboratorului, sa se calculeze si sa se afiseze o descompunere
# LU a matricii A si solutia sistemului Ax = b

def ex5(A, b):
    A = A.dot(A.transpose())
    z = scp.cho_solve(scp.cho_factor(A, True), b)
    print("\nsolutia sistemului folosind librarii: ", z)
    return z


def ex6(A):
    I=np.matrix(np.identity(n))
    A = np.matrix(A.dot(A.transpose()))

    l=I[0]
    x = scp.cho_solve(scp.cho_factor(A, True), np.transpose(np.matrix(l)))
    z=np.matrix(x)
    for l in range(1, len(I)):
        x=scp.cho_solve(scp.cho_factor(A, True), np.transpose(np.matrix(I[l])))
        z=np.append(z, x, axis=1)

    w=scp.inv(A)
    print("\ninversa calculata:         \n", z, "\n")
    print("inversa folosind librarii: \n", w, "\n")
    print("norma: ", scp.norm(z-w))


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

    return n, A, b, eps

def data_tastatura():
    n=int(input("enter n: "))
    A=[]
    for i in range(n):
        a = []
        for j in range(n):
            a.append(float(input()))
        A.append(a)
    b=[]
    for j in range(n):
        b.append(float(input()))

    A = np.array(A)
    b = np.array(b)
    eps=10**-8

    return n, A, b, eps

def data_random():
    n=random.randint(2, 101)

    A = np.random.randint(-20, 21, size=(n, n))
    A = (A + A.T) / 2

    b = np.random.randint(-20, 21, size=(n, 1))
    b = b.T

    A = np.array(A)
    b = np.array(b)
    eps=10**-8

    print(n)
    print(A)
    print(b)

    return n, A, b, eps

n, A, b, eps=data_file()
#n, A, b, eps=data_tastatura()
#n, A, b, eps=data_random()

ex1(A, eps)
ex2(A, eps) #in acest punct, A este o matrice inferior triunghilara
Xchol=ex3(A, eps, b) #in acest punct, A este o matrice inferior triunghilara
ex5(A, b) #in acest punct, A este o matrice inferior triunghilara
ex4(A, Xchol, b) #in acest punct, A este o matrice inferior triunghilara

ex6(A) #in acest punct, A este o matrice inferior triunghilara