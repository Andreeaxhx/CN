import math
import random
from scipy import linalg
import numpy as np
from matplotlib import pyplot as plt


def function1(arg):
    return arg ** 2 - 12 * arg + 30


def function2(arg):
    return math.sin(arg) - math.cos(arg)


def function3(arg):
    return 2 * arg ** 3 - 3 * arg + 15


def deriv_function1(arg):
    return 2 * arg - 12


def deriv_function2(arg):
    return math.cos(arg) + math.sin(arg)


def deriv_function3(arg):
    return 6 * (arg ** 2) - 3


def find_xi(a, b, n):
    x = [a]
    for i in range(0, n - 2):
        val = random.randint(a, b * 100) / 100
        # val = random.randint(a, b)
        while val <= a or val >= b or val in x:
            val = random.randint(a, b * 100) / 100
            # val = random.randint(a, b)
        x.append(val)

    x.append(b)
    x = sorted(x)
    return x


def find_yi(function, x):
    y = []
    for val in x:
        y.append(function(val))
    return y


def matrix_B(m, n, x):
    B = []
    for index in range(0, m + 1):
        B.append([])
        for jndex in range(0, m + 1):
            suma = 0
            for i in range(0, n):
                suma += x[i] ** (index + jndex)
            B[index].append(suma)
    return B


def matrix_f(m, n, x, y):
    f = []
    for index in range(0, m + 1):
        suma = 0
        for i in range(0, n):
            suma += (x[i] ** index) * y[i]
        f.append(suma)
    return f


def horner(x, coef_list):
    result = 0
    for i in range(0, len(coef_list)):
        result = coef_list[i] + (x * result)
    return result


a = float(input("Enter a: "))
b = float(input("Enter b: "))
n = int(input("Enter n: "))
m = int(input("Enter m: "))
function_str = input("Which function: ")
if function_str == "1":
    function = function1
    da = deriv_function1(a)
elif function_str == "2":
    function = function2
    da = deriv_function2(a)
elif function_str == "3":
    function = function3
    da = deriv_function3(a)

print()
x = find_xi(a, b, n)
print("x values: ", x)
y = find_yi(function, x)
print("y values: ", y)

B = matrix_B(m, n, x)
B = np.array(B)
print("\nB: ", B)

f = matrix_f(m, n, x, y)
f = np.array(f)
print("f: ", f)

a = linalg.solve(B, f)
print("a: ", a)

print("verificare (Ba=f): ", B.dot(a))

X = random.choice(x)
a = np.flip(a)
result1 = horner(X, a)

suma = 0
for i in range(0, n):
    suma += math.fabs(horner(x[i], a) - y[i])

print(f"\nPm({X}): ", result1)
print(f"|Pm({X}) − f({X})|: ", math.fabs(result1 - function(X)))
print(f"suma |Pm(xi) − yi|: ", suma)


def Sf(arg, x, y, da):
    result = 0
    A0 = da
    for i in range(0, n - 1):
        if x[i] <= arg <= x[i + 1]:
            hi = x[i + 1] - x[i]
            A1 = -A0 + (2 * (y[i + 1] - y[i])) / hi
            result = ((A1 - A0) / (2 * hi)) * (arg - x[i]) ** 2 + A0 * (arg - x[i]) + y[i]
    return result

result2 = Sf(X, x, y, da)
print(f"\nSf({X}):", result2)
print(f"|Sf(x) − f(x)|: ", math.fabs(result2 - function(X)))

x1 = np.array(x)
function = np.vectorize(function)
plt.title("Graph for function")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plot1 = plt.figure(1)
plt.plot(x1,function(x1))
#plt.show()

x2 = np.array(x)
Y = []
for i in x:
    Y.append(horner(i, a))
plt.title("Pm(x)")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plot2 = plt.figure(2)
plt.plot(x2,Y)
#plt.show()

x3 = np.array(x)
Y = []
for i in x:
    Y.append(Sf(i, x, y, da))
plt.title("Sf(x)")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plot3 = plt.figure(3)
plt.plot(x3,Y)
plt.show()