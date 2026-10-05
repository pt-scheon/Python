data=int(input())
di = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}  
g=[]
if type(data) == int:
    p = list(str(data))
    for k in range(len(p)):
        if int(p[k]) in di:
            g.append((di[int(p[k])]))
def ty(idx):
    if g[idx]=="three":
        g[idx]="thirty"
    elif g[idx]=="two":
        g[idx]="twenty"
    elif g[idx]=="four":
        g[idx]="forty"
    elif g[idx]=="five":
        g[idx]="fifty"
    elif g[idx]=="six":
        g[idx]="sixty"
    elif g[idx]=="seven":
        g[idx]="seventy"
    elif g[idx]=="eight":
        g[idx]="eighty"
    elif g[idx]=="nine":
        g[idx]="ninety"

def wordinbw(g):
    if len(g)>9:
        g.insert(-9,"arab")
        ty(-9)
    if len(g)>7:
        g.insert(-7,"crore")
        ty(-7)
    if len(g)>5:
        g.insert(-5,"lakh")
        ty(-5)
    if len(g)>3:
        g.insert(-3,"thousand")
    if len(g)>2:
        g.insert(-2,"hundred")
    if len(g)>1:
        ty(-2)



print(" ".join(g))
