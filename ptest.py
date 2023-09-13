from math import factorial,comb,perm
def fun(m,n):
    return n**m
def bij(m,n):
    if m==n:
        return factorial(n)
    else:
        return 0
def one2one(m,n):
    if m<=n:
        return perm(n,m)
    else:
        return 0
def on2(m,n):
    sum=0
    if m>=n:
        for k in range(n):
            sum+=(-1)**k*comb(n,n-k)*(n-k)**m
    return sum


m=int(input("enter |a|"))
n=int(input("enter  |b|"))
print( " a to b",fun(m,n))
print(" b to a",fun(n,m))
print(" a to b bijective",bij(m,n))
print(" b to a bijective",bij(n,m))
print(" a to b one to one",one2one(m,n))
print(" b to a one to one",one2one(n,m))
print(" b to a on2",on2(n,m))
print(" ato b on2",on2(m,n))

