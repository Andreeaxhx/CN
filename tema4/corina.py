import numpy as np
import math
def citeste_f(data):
    with open(data, 'r') as f:
        n = int(f.readline())
        f_1 = []
        for line in enumerate(f.readlines()):
            if line[1]=='\n' :
                continue
            elif line[0]>0 and line[0]<n+1:

                val = float(line[1])
                f_1.append(val)
    #print('f=',f_1)
    return f_1

def citeste_tridiag(data):
    with open(data, 'r') as f:
        n = int(f.readline())
        p = int(f.readline())
        q = int(f.readline())
        a = []
        b=[]
        c=[]
        for line in enumerate(f.readlines()):
            if line[1]=='\n' :
                continue
            elif line[0]>0 and line[0]<n+1:

                val = float(line[1])
                a.append(val)
            elif line[0]>n+1 and line[0]<2*n+1:
                val = float(line[1])
                c.append(val)
            else:
                val = float(line[1])
                b.append(val)
    #print(a ,'\n')
    # print(b, '\n')
    # print(c,'\n')
    return a,c,b,n,p,q
# a,c,b,n,p,q=citeste_tridiag('a1')
# f_n=citeste_f('f1')
# a,c,b,n,p,q=citeste_tridiag('a2')
# f_n=citeste_f('f2')
# a,c,b,n,p,q=citeste_tridiag('a3')
# f_n=citeste_f('f3')
a,c,b,n,p,q=citeste_tridiag('a4')
f_n=citeste_f('f4')
# a,c,b,n,p,q=citeste_tridiag('a5.txt')
# f_n=citeste_f('f5.txt')
for i in a:
    if i==0:
        print("eroare")
#print(a.count(0))

def metoda_iterativa(a,b,c,n,f_n,eps):
    x_gs = [0] * len(f_n)
    k=0
    delta_x=100
    while eps <= delta_x <= 10 ** 8 and k <= 10000:
        delta_x=0
        for i in range(len(f_n)):
            if i == 0:
                num = f_n[i] - b[i] * x_gs[1]
                curent = (num / a[i])
                delta_x+=math.fabs(math.fabs(curent)- math.fabs(x_gs[i]))
                x_gs[i]=curent
            elif i == len(f_n) - 1:
                num = f_n[-1] - c[-1] * x_gs[-2]
                curent = (num / a[-1])
                delta_x+= math.fabs(math.fabs(curent)- math.fabs(x_gs[i]))
                x_gs[i]=curent
            else:
                num = f_n[i] - (c[i - 1] * x_gs[i-1] + b[i] * x_gs[i+1])
                curent = (num / a[i])
                delta_x+= math.fabs(math.fabs(curent)- math.fabs(x_gs[i]))
                x_gs[i]=curent
        k+=1

    print ('Nr de iteratii',k)
    if delta_x< eps:
        for i in x_gs:
            print(round(i,4),end=",")
    else:
        print ("Divergenta!!")
    return x_gs

gauss=metoda_iterativa(a,b,c,n,f_n,eps=10**-1)

def verific_cu_norma(a,b,c,xGS,f):
    produs = []
    for i in range(len(a)):
        if i == 0:
            produs.append(a[i]*xGS[i]+b[i]*xGS[i+1])
        elif i == len(a)-1:
            produs.append(c[i-1]*xGS[i-1]+a[i]*xGS[i])
        else:
            produs.append(c[i-1]*xGS[i-1] + a[i]*xGS[i]+b[i]*xGS[i+1])
    # for i in produs:
    #     print(round(i,4),end=',')
    ax_diff_f = np.linalg.norm(np.array(produs)-np.array(f))
    return ax_diff_f


norma = verific_cu_norma(a,b,c,gauss,f_n)
print('Norma este egala cu',norma)