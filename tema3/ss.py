def memorare_matrice_a():
    f = open('a', 'r')
    lines = f.readlines()

    n = int(lines[0])

    A=[]
    for line in range(2, len(lines)):
        lst=[float(i) for i in lines[line].split(", ")]
        linie=int(lst[1])
        coloana=int(lst[2])
        valoare=lst[0]
        if linie<len(A) and coloana in A[linie].keys():
            valoare=valoare+A[linie][coloana]
        A.insert(linie, {coloana:valoare})
    return A

A=memorare_matrice_a()
print(A)