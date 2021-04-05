import scipy.linalg as scp
from functii import ex1, data_file, euclidean_norm
import numpy as np
import math

n, A = data_file()
epsilon = 10 ** -7


def matrix_array_cholesky(A, epsilon):

    distance = 1
    k = 0

    while distance > epsilon and k < 1000:

        L = ex1(A, eps=10**-1)
        LT = np.transpose(L)

        AUX = np.array(LT).dot(np.array(L))

        distance = euclidean_norm(AUX, A)
        print(distance)

        A = AUX
        k += 1
        print("iteratia -", k)
        print("norma: ", distance)

#matrix_array(A, epsilon)

n, A = data_file()
A = np.array([[1,2], [3,4], [5,6]])
u, s, v = np.linalg.svd(A)
print("u: ", u)
print("s: ", s)
print("v: ", v)
