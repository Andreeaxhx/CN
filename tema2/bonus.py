import math
import numpy as np
import scipy.linalg as scp
import random

def ex1(n, A, eps):

    k=0; L=[]; x=n
    for i in range(0, len(A)):
        print("k-----", k)
        suma=0; z=n-1
        if i==k:
            print("i egal cu k")
            for q in range(0, i):
                if q==i-z:
                    suma+=(A[q]**2)
                    print("suma--", i, "-" , suma)
                    z-=1
            L.append(math.sqrt(A[i]-suma))
            k+=x
            x-=1
        else:
            L.append(A[i]/L[0])





    """for j in range(0, len(A)):
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
    print("L * L transpus = A: \n", A.dot(A.transpose()))"""
    return L

def data_file():
    file1 = open('data_bonus', 'r')
    line = file1.read()
    A=[]; b=[]
    n=int(line[0])
    l = line.split(" ");
    i=1
    while(len(A)!=n*(n+1)/2):
        A.append(int(l[i]))
        i+=1
    while(len(b)!=n):
        b.append(int(l[i]))
        i+=1
    eps = 10**-8

    return n, A, b, eps

n, A, b, eps=data_file()

print(n)
print(A)
print(b)
print("L-----", ex1(n, A, eps))