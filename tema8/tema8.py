from scipy.misc import derivative
import math


def derivative1(f, x):
    h = 10 ** -5
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)


def derivative2(f, x):
    h = 10 ** -5
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def second_derivative(f, x):
    h = 10 ** -5
    return (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * (h ** 2))


def f(x):
    return 1/3 * x**3 - 2 * x ** 2 + 2 * x + 3
    # return x ** 2 + math.sin(x)
    # return x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4


def Dehghan_Hajarian_deriv1(epsilon):
    x0 = 0
    k = 0

    x1 = x0

    if math.fabs(derivative1(f, x1 + derivative1(f, x1)) - derivative1(f, x1)) <= epsilon:
        return x1, k

    z = x1 + ((derivative1(f, x1) ** 2) / (derivative1(f, x1 + derivative1(f, x1)) - derivative1(f, x1)))
    delta_x = (derivative1(f, x1) * (derivative1(f, z) - derivative1(f, x1))) / (derivative1(f, x1 + derivative1(f, x1)) - derivative1(f, x1))

    x1 = x1 - delta_x

    while 10**8 >= math.fabs(delta_x) >= epsilon and k <= 1000:
        if math.fabs(derivative(f, x1 + derivative(f, x1)) - derivative(f, x1)) <= epsilon:
            return x1, k

        z = x1 + ((derivative1(f, x1) ** 2) / (derivative1(f, x1 + derivative1(f, x1)) - derivative1(f, x1)))
        delta_x = (derivative1(f, x1) * (derivative1(f, z) - derivative1(f, x1))) / (
                    derivative1(f, x1 + derivative1(f, x1)) - derivative1(f, x1))

        x1 = x1 - delta_x

        k += 1

    if math.fabs(delta_x) < epsilon:
        return x1, k
    else:
        print("divergenta")


def Dehghan_Hajarian_deriv2(epsilon):
    x0 = 3
    k = 0

    x1 = x0

    if math.fabs(derivative2(f, x1 + derivative2(f, x1)) - derivative2(f, x1)) <= epsilon:
        return x1, k

    z = x1 + ((derivative2(f, x1) ** 2) / (derivative2(f, x1 + derivative2(f, x1)) - derivative2(f, x1)))
    delta_x = (derivative2(f, x1) * (derivative2(f, z) - derivative2(f, x1))) / (derivative2(f, x1 + derivative2(f, x1)) - derivative2(f, x1))

    x1 = x1 - delta_x

    while 10**8 >= math.fabs(delta_x) >= epsilon and k <= 1000:
        if math.fabs(derivative(f, x1 + derivative(f, x1)) - derivative(f, x1)) <= epsilon:
            return x1, k

        z = x1 + ((derivative2(f, x1) ** 2) / (derivative2(f, x1 + derivative2(f, x1)) - derivative2(f, x1)))
        delta_x = (derivative2(f, x1) * (derivative2(f, z) - derivative2(f, x1))) / (
                    derivative2(f, x1 + derivative2(f, x1)) - derivative2(f, x1))

        x1 = x1 - delta_x

        k += 1

    if math.fabs(delta_x) < epsilon:
        return x1, k
    else:
        print("divergenta")

epsilon = 10 ** -6

minim1, k = Dehghan_Hajarian_deriv1(epsilon)
print("punct de minim: ", Dehghan_Hajarian_deriv1(epsilon)[0])
print(f"F''({minim1}): ", second_derivative(f, minim1))
print(f"F''({minim1}) > 0:", second_derivative(f, minim1) > 0)
print("nr. iteratii: ", k)
if second_derivative(f, minim1) > 0:
    print(f"punctul {minim1} este punct de minim pentru functia F")

print()

minim2, k = Dehghan_Hajarian_deriv2(epsilon)
print("punct de minim: ", Dehghan_Hajarian_deriv2(epsilon)[0])
print(f"F''({minim2}): ", second_derivative(f, minim2))
print(f"F''({minim2}) > 0:", second_derivative(f, minim2) > 0)
print("nr. iteratii: ", k)
if second_derivative(f, minim2) > 0:
    print(f"punctul {minim2} este punct de minim pentru functia F")