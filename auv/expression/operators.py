
op = input("").split()
opn = []
opr = []
for i in range(len(op)):
    if i % 2 == 0:
        num=ord(op[i].upper()) - 64
        opn.append(num)
    else:
        opr.append(op[i])
r = opn[0]
for g in range(len(opr)):
    operator = opr[g]
    num1 = opn[g + 1]
    if operator == '+':
        r+=num1
    elif operator == '-':
        r-=num1
print(r)





