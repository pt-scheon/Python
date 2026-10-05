def ty(l,idx):
    if l[idx]=="three":
        l[idx]="thirty"
    elif l[idx]=="two":
        l[idx]="twenty"
    elif l[idx]=="four":
        l[idx]="forty"
    elif l[idx]=="five":
        l[idx]="fifty"
    elif l[idx]=="six":
        l[idx]="sixty"
    elif l[idx]=="seven":
        l[idx]="seventy"
    elif l[idx]=="eight":
        l[idx]="eighty"
    elif l[idx]=="nine":
        l[idx]="ninety"
def wordinbw(lis):
    if len(lis)>9:
        lis.insert(-9,"arab")
    if len(lis)>7:
        lis.insert(-7,"crore")
        if len(lis)>9:
            ty(lis, -10)
    if len(lis)>5:
        lis.insert(-5,"lakh")
        if len(lis)>9:
            ty(lis, -8)
    if len(lis)>3:
        lis.insert(-3,"thousand")
        ty(lis, -6)
    if len(lis)>2:
        lis.insert(-2,"hundred")
    if len(lis)>1:
        ty(lis, -2)
    return " ".join(lis) 
def interchange(data):
    di = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}  
    g=[]
    if type(data) == int:
        p = list(str(data))
        for k in range(len(p)):
            if int(p[k]) in di:
                g.append((di[int(p[k])]))

        return wordinbw(g)
    if type(data) == str:
        for k, v in di.items():
            if v == data:
                return k
d = {"zero":3443128,"two":38}

c = {interchange(n): interchange(w) for w,n in d.items()}
print(c)