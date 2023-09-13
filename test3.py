

expression="not((p or q)and(not p or r) and not(q or r)) or r"
expression=expression.replace("and","&")
expression=expression.replace("or","|")
expression=expression.replace("not","~")
print(" logical expression")
print("X=")
print(expression)
X=[]
print("truth table is")
print("------------------")
print("| p | q | r | x |")
print("-------------------")
for p in range(0,2):
    for q in range(0,2):
        for r in range(0,2):
            x=abs(eval(expression))
            X.append(x)
            print("|"+str(p)+ " | "+str(q)+" | "+str(r)+" | "+str(x)+" | ")
check=all(i==X[0] for i in X)
if check:
    if check==0:
        print(" conjugation")
    else:
        print("totology")
else:
    print(" nor totology nor conju")