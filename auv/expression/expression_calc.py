n=list(input())

def calculate(expr):
    operators=[]
    num=[]
    i=0
    while i<len(expr):
        if expr[i] == "(":
            start=i
            count=1
            i+=1
            while count!=0:
                if expr[i]=="(":
                    count += 1
                elif expr[i]==")":
                    count-=1
                i+=1
            value=calculate(expr[start+1:i-1])
            num.append(value)
        else:
            if 64<ord(expr[i])<91:
                num.append(ord(expr[i]) - 64)
            elif 96 < ord(expr[i]) < 123:
                num.append(ord(expr[i]) - 96)
            elif expr[i] in "+-*/%":
                operators.append(expr[i])
            i+=1
    i=0
    while i<len(operators):
        if operators[i] == "*":
            num[i] = num[i]*num[i+1]
            num.pop(i+1)
            operators.pop(i)
        elif operators[i] == "/":
            num[i] = num[i] / num[i+1]
            num.pop(i + 1)
            operators.pop(i)
        elif operators[i] == "%":
            num[i] = num[i] % num[i+1]
            num.pop(i + 1)
            operators.pop(i)
        else:
            i+=1
    r=num[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            r+=num[i + 1]
        elif operators[i] == "-":
            r-=num[i + 1]
    return r
print(calculate(n))
