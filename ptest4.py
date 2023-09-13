from math import comb
print("ho")
print("h1")
x=[0,1,2,3,4]
f=[5,29,36,25,5]
Eoi=sum(f)
n=len(x)-1
p=float(input("print p"))
q=1-p
px=[comb(n,i)*p**i*q**(n-i) for i in x]
Ei=[Eoi*i for i in px]
EEi=sum(Ei)
print(" ei  ",end=" ")
for i in Ei:
    print( i ,end="   ")
print("\n")
print("Eoi= ",Eoi)
print("EEi= ",EEi)
flag=[(f[i]-Ei[i])**2/Ei[i] for i in range(len(f))]
X2=sum(flag)
print("X2=",X2)
df=n
X2tab=float(input("enter tab value"))
if X2<=X2tab:
    print("ho")
else:
    print("h1")
