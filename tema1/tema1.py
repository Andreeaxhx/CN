import math
import time
import random

# 1. Find the smallest positive number u > 0, written as a negative power of 10, u = 10**(−m), which satisfies the property:
# 1.0 + u != 1.0.

def smallest():
    m = 1
    while True:
        u = 10 ** -m
        if 1.0 + u == 1.0:
            return u * 10
        else:
            m += 1

print("\n1. smallest positive number, written as a negative power of 10:", smallest())

# 2. Operation + is non-associative: consider the numbers a = 1.0, b = u/10, c = u/10,
# where u is the above computed machine precision. Verify that the computer addition operation is non-associative,
# i.e.: (a + b) + c != a + (b + c).
# Find an example that shows the computer multiplication operation is also non associative.

a = 1.0
b = smallest() / 10
c = smallest() / 10

sum1 = (a + b) + c
sum2 = a + (b + c)

print("\n2. operation + is non-associative: ", sum1, " != ", sum2)

a = 1.01
b = smallest() / 10
c = smallest() / 10
prod1 = (a * b) * c
prod2 = a * (b * c)

print("\n   operation * is non-associative: ", prod1, " != ", prod2)

# 3.
print("3.")

argument = math.pi*5/6
while argument<=-math.pi/2 or argument>=math.pi/2:
    argument=argument-math.pi
print("tan(x):            ", math.tan(argument))

def my_tan_functii(x, epsilon):
    mic = 10 ** -12
    f = mic
    C = f
    D = 0

    a = x
    b = 1

    D = b + a * D
    if D == 0: D = mic
    D = 1 / D

    C = b + (a / C)
    if C == 0: C = mic

    delta = C * D
    f = delta * f
    j = 2

    while abs(delta - 1) >= epsilon:

        a = -(x * x)
        b = j * 2 - 1

        D = b + (a * D)
        if D == 0: D = mic
        D = 1 / D

        C = b + (a / C)
        if C == 0: C = mic

        delta = C * D
        f = delta * f

        j = j + 1

    return f

err_functii=abs(math.tan(argument) - my_tan_functii(argument, 10 ** -12))
print("my_tan_functii(x): ", my_tan_functii(argument, 10 ** -12))

def my_tan_poli(x):
    ok=0
    if x >= math.pi / 4 and x < math.pi / 2:
        x = (math.pi / 2) - x
        ok=1
    c1 = 1 / 3
    c2 = 2 / 15
    c3 = 17 / 315
    c4 = 62 / 2835
    x2=x*x
    x3=x2*x
    x5=x3*x2
    x7=x5*x2
    x9=x7*x2
    P=x+c1*x3+c2*x5+c3*x7+c4*x9

    if ok==1: return 1/P
    return P

err_poli=abs(math.tan(argument) - my_tan_poli(argument))
print("my_tan_poli(x):    ", my_tan_poli(argument))


print("\n|tan(x) − my_tan_poli(x)|:    ", err_poli)
print("|tan(x) − my_tan_functii(x)|: ", err_functii)

start = time.time()
#-------------------------------------------
for i in range(1, 10001):
    x=random.uniform(-math.pi/2, math.pi/2)
    my_tan_functii(x, 10**-12)
#-------------------------------------------
end = time.time()

print("\ntime of my_tan_functii: ", end - start)

start1 = time.time()
#-------------------------------------------
for i in range(1, 10001):
    x=random.uniform(-math.pi/2, math.pi/2)
    my_tan_poli(x)
#-------------------------------------------
end1 = time.time()

print("time of my_tan_poli:    ", end1 - start1)


if err_functii>err_poli:
    print("\naproximarea functiei tangenta folosind fractii continue are eroare mai mare")
else:
    print("\naproximarea functiei tangenta folosind polinoame are eroare mai mare")


if (end-start>end1-start1):
    print("aproximarea functiei tangenta folosind fractii continue are timp de executie mai mare")
else:
    print("aproximarea functiei tangenta folosind polinoame are timp de executie mai mare")