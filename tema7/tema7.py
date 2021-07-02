import math


def find_R(coef_list):
    A = max(coef_list)
    R = (coef_list[0] + A) / coef_list[0]

    return R


def horner(x, coef_list):
    result = 0
    for i in range(0, len(coef_list)):
        result = coef_list[i] + (x * result)

    # print("coef. list for polynom P: ", coef_list)
    # print(f"value of P polynom in {x}: ", result)
    return result


def P_derivat_x(P, x):
    coef_list = []
    for i in range(len(P) - 1):
        coef_list.append(P[i] * (len(P) - i - 1))

    result = horner(x, coef_list)

    # print("coef. list for the 1st derivative: ", coef_list)
    # print(f"value of P' polynom in {x}: ", result)
    return result


def P_sescund_x(P, x):
    coef_list = []
    for i in range(len(P) - 2):
        coef_list.append(P[i] * (len(P) - i - 1) * (len(P) - i - 2))

    result = horner(x, coef_list)

    # print("coef. list for the 2nd derivative: ", coef_list)
    # print(f"value of P\" polynom in {x}: ", result)
    return result


def Olvers_Method(coef_lost, x0, epsilon):
    k = 0
    # print(x0)

    P_x = horner(x0, coef_list)
    P_prim_x = P_derivat_x(coef_list, x0)
    # print(P_prim_x)
    if math.fabs(P_prim_x) >= epsilon:

        P_sec_x = P_sescund_x(coef_list, x0)

        c_k = ((P_x ** 2) * P_sec_x) / (P_prim_x ** 3)
        # print(c_k)
        # print(P_x / P_prim_x)
        delta_x = (P_x / P_prim_x) + ((1 / 2) * c_k)
        x1 = x0 - delta_x

        x0 = x1
        # print(delta_x)

        while epsilon <= math.fabs(delta_x) <= 10 ** 8 and k <= 1000:
            if math.fabs(P_prim_x) <= epsilon:
                break
            else:
                P_x = horner(x0, coef_list)
                P_prim_x = P_derivat_x(coef_list, x0)
                P_sec_x = P_sescund_x(coef_list, x0)

                c_k = ((P_x ** 2) * P_sec_x) / (P_prim_x ** 3)
                delta_x = (P_x / P_prim_x) + ((1 / 2) * c_k)
                x1 = x0 - delta_x

                # print(f"iteratia {k}: ", math.fabs(x1 - x0))

                # print("x0 =", x0)
                x0 = x1
                k += 1

        if delta_x < epsilon:
            # print("xk aprox. equal x*: ", x1)
            return x1
        else:
            print("divergence")


# coef_list = [1, -6, 11, -6]

# coef = [42, -55, -42, 49, -6]
# coef_list = [1/42 * i for i in coef]

coef = [8, -38, 49, -22, 3]
coef_list = [1/8 * i for i in coef]

# coef_list = [1, -6, 13, -12, 4]

R = find_R(coef_list)
print(f"\nthe range is [{-R}, {R}]")

epsilon = 10 ** -7

radacini = []

for x0 in range(int(-R), int(R) + 1):  # while len(radacini) < len(coef_list) - 1:

    rad = Olvers_Method(coef_list, x0, epsilon)
    if rad:
        radacini.append(rad)

    rad = Olvers_Method(coef_list, x0 / 10, epsilon)
    if rad:
        radacini.append(rad)

print("\nall roots: ", radacini)
radd = [radacini[0]]

for i in radacini:
    ok = 1
    for j in radd:
        if math.fabs(i - j) < epsilon:
            ok = 0
    if ok == 1:
        radd.append(i)

print("\nunique values: ", radd)

f = open("data.txt", "a")
f.write("coef. list: ")
f.write(str(coef_list))
f.write("\n")
f.write("roots: ")
f.write(str(radd))
f.write("\n")
f.close()
