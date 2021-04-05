import math

mat=[
     [[2.5, 2], [102.5, 0]],
     [[3.5, 0], [0.33, 4], [1.05, 2], [104.88, 1]],
     [[100, 2]],
     [[1.3, 1], [101.3, 3]],
     [[1.5, 3], [0.73, 0], [102.23, 4]]
     ]

a=[102.5, 104.88, 100, 101.3, 102.23]
b=[2.5, 1.05, 0.33, 0]
c=[3.5, 1.3, 0.73, 1.5]

copie2=mat.copy()
n=len(copie2)

for i in range(n):
    for k in range(len(copie2[i])):
        if i==copie2[i][k][1]:
            copie2[i][k][0]+=a[i]
        elif 1==copie2[i][k][1]-i:
            copie2[i][k][0] += b[copie2[i][k][1]-1]
        elif i==copie2[i][k][1]+1:
            copie2[i][k][0] += c[copie2[i][k][1]]


x=[lista[1] for lista in copie2[0]]

if 0 not in x:
    copie2[0].append([a[0], 0])
if 1 not in x:
    copie2[0].append([b[0], 1])

for i in range(1, n-1):
    x=[lista[1] for lista in copie2[i]]

    if i-1 not in x:
        copie2[i].append([c[i - 1], i - 1])

    if i not in x:
        copie2[i].append([a[i], i])

    if i+1 not in x:
        copie2[i].append([b[i], i + 1])

x=[lista[1] for lista in copie2[n-1]]

if n-1 not in x:
    copie2[n-1].append([a[n-1], n-1])
if n-2 not in x:
    copie2[n-1].append([c[n-1], n-2])

"""print("matricea suma: \n")
for i in copie2:
    print(i)
"""
def diferenta_in_modul(mat, mat_de_verificare):

    eps=10**-7
    for linie in range(len(mat)):
        mat[linie].sort(key = lambda x: x[1])
        mat_de_verificare[linie].sort(key = lambda x: x[1])

        for lista in range(len(mat[linie])):
            if math.fabs(mat[linie][lista][0]-mat_de_verificare[linie][lista][0])>eps:
                print("matricea mea:    linia ", linie, " - ", mat[linie][lista])
                print("matricea profei: linia ", linie, " - ", mat_de_verificare[linie][lista])







def prod(A, a, b, c, p, q, eps):

    PROD=[]
    in_plus=0
    for line in range(0, len(A)):
        for column in A[line].keys():
            PROD.insert(len(PROD), {})

            if column-1>=0:
                PROD[line][column - 1] = c[column - 1] * A[line][column] + in_plus

            PROD[line][column] = a[column] * A[line][column] + in_plus
            in_plus=0

            if column<len(b):
                PROD[line][column+1] = b[column] * A[line][column] + in_plus

    return PROD

mat=[
     [[2.5, 2], [102.5, 0]],
     [[3.5, 0], [0.33, 4], [1.05, 2], [104.88, 1]],
     [[100, 2]],
     [[1.3, 1], [101.3, 3]],
     [[7, 3], [0.73, 0], [102.23, 4]]
     ]
mat_de_verificare=[
     [[2.5, 2], [102.5, 0]],
     [[3.5, 0], [0.33, 4], [1.05, 2], [104.88, 1]],
     [[100, 2]],
     [[1.3, 1], [101.3, 3]],
     [[1.5, 3], [0.73, 0], [102.23, 4]]
     ]

diferenta_in_modul(mat, mat_de_verificare)