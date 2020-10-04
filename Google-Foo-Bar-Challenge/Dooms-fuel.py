from itertools import product 
from fractions import Fraction
from functools import reduce
def invert(matrix):
    n = len(matrix)
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]
    for i in range(n):
        inverse[i][i] = Fraction(1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return 
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return 
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse
def sumRow(m, r):
    return sum(m[r])
def substract(matr_a, matr_b):
    output = []
    for i in range(len(matr_a)):
        tmp = []
        for valA, valB in zip(matr_a[i], matr_b[i]):
            tmp.append(valA - valB)
        output.append(tmp[:])
    return output[:]
def matrixmult(matr_a, matr_b):
    rows = len(matr_b)
    if rows != 0:
        cols = len(matr_b[0])
    else:
        cols = 0
    resRows = range(len(matr_a))
    rMatrix = [[0] * cols for _ in resRows]
    for idx in resRows:
        for j, k in product(range(cols), range(rows)):
            rMatrix[idx][j] += matr_a[idx][k] * matr_b[k][j]
    if cols != 0:
        return rMatrix
    else:
        return 0
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a
def lcm(a,n):
    ans = a[0]
    for i in range(1,n):
        ans = (a[i]*ans)//gcd(a[i],ans)
    return ans
def solution(m):
    if len(m) == 1:
        return [1, 1]
    num = len(m)
    f=[]
    for i in range(0,num):
        j=[]
        j.append(sumRow(m,i))
        j.append(i)
        f.append(j)
    k=0;
    for i in range(0,num):
        for j in range(0,num):
            if f[i][0]!=0:
                m[i][j]=Fraction(m[i][j],f[i][0])
    j=[]
    for i in range(0,len(f)):
        if f[i][0].numerator==0:
            j.append(i)
            del m[f[i][1]-k]
            k=k+1
    q=m
    k=[]
    t=0
    e=m
    q=[]
    for i in range(0,len(m)):
        row=[]
        for r in range(0,len(m[0])):
            for t in range(0,len(j)):
                if j[t] is r:
                    row.append(m[i][r])
        q.append(row)
    t=0;
    w=0;
    e=[]
    for i in range(0,len(m)):
        row=[]
        flag=1
        for r in range(0,len(m[0])):
            for t in range(0,len(j)):
                if j[t] is r:
                    flag=0
                    break
            if flag == 1:
                row.append(m[i][r])
        e.append(row)
    l=[]
    for i in range(0,len(e)):
        k=[]
        for b in range(0,len(e)):
            if i==b:
                k.append(1)
            else:
                k.append(0)
        l.append(k)
    l=substract(l,e)
    l=invert(l)
    r = matrixmult(l,q)
    if r == 0:
        return 0
    else:
        m =r[0]
    e=[]
    for i in range(0,len(m)):
        e.append(m[i].denominator)
    k=lcm(e,len(e))
    e=[]
    for i in range(0,len(m)):
        e.append((m[i].numerator*k)//m[i].denominator)
    e.append(k)
    
    return e

m=[
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
print(solution(m))