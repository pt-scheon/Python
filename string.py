s=input()

def upperr(p):
    result = ""
    for char in p:
        if ord(char)>64 and ord(char)<91:
            result += char
        elif ord(char)>96 and ord(char)<123:
            result+=chr(ord(char)-32)
        else: 
            result+= char
    return result
def lowerr(p):
    result = ""
    
    for char in p:
        if ord(char)>96 and ord(char)<123:
            result+=char
        elif ord(char)>64 and ord(char)<91:
            result+=chr(ord(char)+32)
        else: 
            result += char
    
    return result
def cap(p):
    p=p.split()
    q=list(p)
    for i in range(len(q)):
        if ord(q[i][0])>96 and ord(q[i][0])<123:
            q[i]=chr(ord(q[i][0])-32)+q[i][1:]
    return " ".join(q)
def stripp(p):
    j=""
    for char in p:
        if char==" ":
            pass
        else:
            j += char
    return j
def replacee(p, i, j):
    r=""
    n=0

    while n < len(p):
        if p[n:n+len(i)]==i:
            r += j
            n += len(i)
        else:
            r += p[n]
            n += 1
    return r
def sw(p,i):
    if p[0:len(i)]==i:
        return True
    else:
        return False
def ew(p,i):
    if p[len(p)-len(i):len(p)]==i:
        return True
    else:
        return False
def titlee(p):
    p=p.split()
    q=list(p)
    for i in range(len(q)):
        if ord(q[i][0])>96 and ord(q[i][0])<123:
            q[i]=chr(ord(q[i][0])-32)+q[i][1:]
    return " ".join(q)
def findd(p,i):
    for w in range(len(p)):
        if p[w:w+len(i)]==i:
            return w
    return -1
def islowerr(p):
    for char in p:
        if ord(char)>96 and ord(char)<123:
            pass
        elif ord(char)>=65 and ord(char)<=90:
            return False
    return True
            
def isupperr(p):
    for char in p:
        if ord(char)>=65 and ord(char)<=90:
            pass
        elif ord(char)>=97 and ord(char)<=122:
            return False
    return True
def isspacee(p):
    if len(p)==0:
        return False
    for char in p:
        if char!=" ":
            return False
    return True
def joinn(p, sep):
    result = ""
    for i in range(len(p)):
        result += p[i]
        if i!=len(p)-1:
            result += sep
    return result   
def isdigitt(p):
    for char in p:
        if ord(char)>=48 and ord(char)<=57:
            pass
        else:
            return False
    return True
def rjustt(p,width):
    g=""
    g=(" "*(len(p)-width))+p
    return g
def ljustt(p,width):
    g=""
    g=p+(" "*(width-len(p)))+"hi"
    return g
def centerr(p,width):
    spaces=width-len(p)
    left=spaces//2
    right=spaces-left
    g=(" "*left)+p+(" "*right)
    return g
def countt(p,i):
    u=0
    for r in range(len(p)):
        if p[r:r+len(i)]==i:
            u=u+1
    return u
def splitt(p):
    result = []
    word = ""
    for char in p:
        if char == " ":
            result.append(word)
            word = ""
        else:
            word += char
    result.append(word)
    return result

N=int(input())

for i in range(N):
    func,*line=input().split()

    if func=="upper":
        s=upperr(s)

    elif func=="lower":
        s=lowerr(s)

    elif func=="cap":
        s=cap(s)

    elif func=="strip":
        s=stripp(s)

    elif func=="replace":
        p=line[0]
        q=line[1]
        s=replacee(s,p,q)

    elif func=="sw":
        p=line[0]
        print(sw(s,p))

    elif func=="ew":
        p=line[0]
        print(ew(s,p))

    elif func=="title":
        s=titlee(s)

    elif func=="find":
        p=line[0]
        print(findd(s,p))

    elif func=="rjust":
        p=int(line[0])
        s=rjustt(s,p)

    elif func=="ljust":
        p=int(line[0])
        s=ljustt(s,p)

    elif func=="center":
        p=int(line[0])
        s=centerr(s,p)

    elif func=="count":
        c=line[0]
        print(countt(s,c))

    elif func=="islower":
        print(islowerr(s))

    elif func=="isupper":
        print(isupperr(s))

    elif func=="isspace":
        print(isspacee(s))

    elif func=="isdigit":
        print(isdigitt(s))

    elif func=="split":
        s=splitt(s)

    elif func=="join":
        m=line[0]
        print(joinn(splitt(s),m))

    elif func=="print":
        print(s)

# print(upperr(s))
# print(lowerr(s))
# print(cap(s))
# print(stripp(s))
# print(replacee(s,"aa","a"))
# print(sw(s,"aa"))
# print(ew(s,"aa"))
# print(titlee(s))
# print(findd(s,"sh"))
# print(rjustt(s,5))
# print(ljustt(s,5))
# print(centerr(s,5))
# print(countt(s,"a"))
# print(islowerr(s))
# print(isupperr(s))
# print(isspacee(s))
# print(isdigitt(s))
# print(splitt(g))
# print(joinn())

