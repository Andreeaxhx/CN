import numpy as np
from numpy import linalg as LA
from numpy import array, identity, diagonal
from math import sqrt

import time

# the matrix in question
a = np.array([[0,0,1], [0,0,1], [1,1,1]])
#a1 = np.array([[4., 1., -2., 2.], [1., 2., 0., 1.], [-2., 0., 3., -2.], [2., 1., -2., -1.]])
#a2 = np.array([[4., 2., 2., 1.], [2., -3., 1., 1.], [2., 1., 3., 1.], [1., 1., 1., 2.]])

# ... or generate a random symmetric matrix
ndim = 5
mt = np.zeros((ndim, ndim))
for dim in range(ndim, 0, -1):
    v = 10 * np.random.rand(dim)
    if dim == ndim:
        mt = np.diag(v)
    else:
        exdim = ndim - dim
        mt += np.diag(v, -exdim) + np.diag(v, exdim)

a = np.copy(mt)

# internally obtained eigen vals/vecs from numpy
print("matrix\n", a)
#tic0 = time.clock()
w, v = LA.eigh(a)
print("\n---Internal numpy method:--\n")

#print("Numpy time", time.clock() - tic0)

print("eigenvalues:\n", w)
print("vectors:\n", v)


# Jacobi method from http://w3mentor.com/learn/python/scientific-computation/python-code-for-solving-eigenvalue-problem-by-jacobis-method/

def jacobi(ain, tol=1.0e-9):  # Jacobi method

    def maxElem(a):  # Find largest off-diag. element a[k,l]
        n = len(a)
        aMax = 0.0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(a[i, j]) >= aMax:
                    aMax = abs(a[i, j])
                    k = i;
                    l = j
        return aMax, k, l

    def rotate(a, p, k, l):  # Rotate to make a[k,l] = 0
        n = len(a)
        aDiff = a[l, l] - a[k, k]
        if abs(a[k, l]) < abs(aDiff) * 1.0e-36:
            t = a[k, l] / aDiff
        else:
            phi = aDiff / (2.0 * a[k, l])
            t = 1.0 / (abs(phi) + sqrt(phi ** 2 + 1.0))
            if phi < 0.0: t = -t
        c = 1.0 / sqrt(t ** 2 + 1.0);
        s = t * c
        tau = s / (1.0 + c)
        temp = a[k, l]
        a[k, l] = 0.0
        a[k, k] = a[k, k] - t * temp
        a[l, l] = a[l, l] + t * temp
        for i in range(k):  # Case of i < k
            temp = a[i, k]
            a[i, k] = temp - s * (a[i, l] + tau * temp)
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(k + 1, l):  # Case of k < i < l
            temp = a[k, i]
            a[k, i] = temp - s * (a[i, l] + tau * a[k, i])
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(l + 1, n):  # Case of i > l
            temp = a[k, i]
            a[k, i] = temp - s * (a[l, i] + tau * temp)
            a[l, i] = a[l, i] + s * (temp - tau * a[l, i])
        for i in range(n):  # Update transformation matrix
            temp = p[i, k]
            p[i, k] = temp - s * (p[i, l] + tau * p[i, k])
            p[i, l] = p[i, l] + s * (temp - tau * p[i, l])

    a = np.copy(ain)
    n = len(a)
    maxRot = 5 * (n ** 2)  # Set limit on number of rotations
    p = identity(n) * 1.0  # Initialize transformation matrix
    for i in range(maxRot):  # Jacobi rotation loop
        aMax, k, l = maxElem(a)
        if aMax < tol: return diagonal(a), p
        rotate(a, p, k, l)
    print(    'Jacobi method did not converge')


print("\n---Jacobi method:---\n")

#tic = time.clock()
wj, vj = jacobi(a)

#print("Jacobi time", time.clock() - tic)
print("eigenvalues:\n", wj)
print("vectors:\n", vj)


# from NR: Householder reduction to tridiagonal form, as in num. rec.

def housetrid(ain, tol=1.0e-9):
    def sign(aa, bb):
        if bb < 0:
            return -abs(aa)
        else:
            return abs(aa)

    n = len(ain)
    d = np.zeros(n)
    e = np.zeros(n)
    b = np.copy(ain)  # local copy
    eia = np.eye(n)
    for i in range(n - 1, 0, -1):
        l = i - 1
        h = 0.
        scale = 0.
        if l > 0:
            u = np.copy(b[i, :l + 1])
            for el in u:
                scale += abs(el)
            if scale == 0.:
                e[i] = b[i, l]
            else:
                h = np.dot(u, u)
                f = b[i, l]
                g = -sign(np.sqrt(h), f)
                e[i] = g
                u[l] = u[l] + np.sign(u[l]) * np.linalg.norm(u)
                h = np.linalg.norm(u)
                u.resize(n)  # zero padded dim to be multiplied with a
                w = u / h
                pp = np.identity(n) - 2 * np.outer(w, w)
                eia = np.dot(pp, eia)
                p = np.dot(b, w)
                k = np.dot(w, p)
                q = p - k * w
                b -= (2 * np.outer(q, w) + 2 * np.outer(w, q))
        else:
            e[i] = b[i, l]
        d[i] = h
    d[0] = 0.
    e[0] = 0.
    for i in range(0, n):
        d[i] = b[i, i]
    return d, e, eia.T


# from NR: reduce tridiagonal matrix to diagonal via QL decomposition and
# Givens rotations - iterative method!

def qlnr(d, e, z, tol=1.0e-9):
    n = len(d)
    e = np.roll(e, -1)  # reorder
    itmax = 1000
    for l in range(n):
        for iter in range(itmax):
            m = n - 1
            for mm in range(l, n - 1):
                dd = abs(d[mm]) + abs(d[mm + 1])
                if abs(e[mm]) + dd == dd:
                    m = mm
                    break
                if abs(e[mm]) < tol:
                    m = mm
                    break
            if iter == itmax - 1:
                print("too many iterations", iter)
                exit(0)
            if m != l:
                g = (d[l + 1] - d[l]) / (2. * e[l])
                r = np.sqrt(g * g + 1.)
                g = d[m] - d[l] + e[l] / (g + np.sign(g) * r)
                s = 1.
                c = 1.
                p = 0.
                for i in range(m - 1, l - 1, -1):
                    f = s * e[i]
                    b = c * e[i]
                    if abs(f) > abs(g):
                        c = g / f
                        r = np.sqrt(c * c + 1.)
                        e[i + 1] = f * r
                        s = 1. / r
                        c *= s
                    else:
                        s = f / g
                        r = np.sqrt(s * s + 1.)
                        e[i + 1] = g * r
                        c = 1. / r
                        s *= c
                    g = d[i + 1] - p
                    r = (d[i] - g) * s + 2. * c * b
                    p = s * r
                    d[i + 1] = g + p
                    g = c * r - b
                    for k in range(n):
                        f = z[k, i + 1]
                        z[k, i + 1] = s * z[k, i] + c * f
                        z[k, i] = c * z[k, i] - s * f
                d[l] -= p
                e[l] = g
                e[m] = 0.
            else:
                break
    return d, z


def householder(ain, tol=1.0e-9):
    a = np.copy(ain)
    diags, extradiags, qq = housetrid(a)
    eigenvals, eigenvecs = qlnr(diags, extradiags, qq)

    print("---tests for householder\n:")
    print("matrix\n", a)
    t = np.diag(diags) + np.diag(extradiags[1:], -1) + np.diag(extradiags[1:], 1)
    print("tridiagonal=\n", t)
    print( "transform Q:\n", qq)
    print("transform test Q.T A Q")
    print( np.dot(qq.T, np.dot(a, qq)))
    print("\n")

    return eigenvals, eigenvecs


print("\n---Householder method:---\n")

#tic2 = time.clock()
eigenvals, eigenvecs = householder(a)

#print("Householder time", time.clock() - tic2)
print("eigenvalues:\n", eigenvals)
print("vectors:\n", eigenvecs)

print("\n eigenvalue test: A.vec-labda.vec must be zero!\n")
for i in range(len(a)):
    p = eigenvecs[:, i]
    print( "eigen vector:\n", np.dot(a, p) - eigenvals[i] * p)

#tic3 = time.clock()
print("\n compare to external routine:\n")
w2, v = LA.eigh(a)

#print("Numpy time again:", time.clock() - tic3)

print("eigenvalues:\n", w2)
print("vectors:\n", v)
print("\n eigenvalue test: A.vec-labda.vec must be zero!\n")
for i in range(len(a)):
    p = v[:, i]
    print("eigen vector:\n", np.dot(a, p) - w2[i] * p)

# compare the sorted eigenvalues

print("\n Jacobi:\n", np.sort(wj))
print("\n Householder:\n", np.sort(eigenvals))
print("\n Numpy native:\n", np.sort(w2))