s=input()
done=True
d1one=True
d2one=True
d3one=True
for char in s:
    if s.isalnum()==True:
        print(True)
    else:
        print(False)
    if  (ord(char)>64 and ord(char)<91) or (ord(char)>96 and ord(char)<123) and d3one==True:
        print(True)
        d3one=False
    else:
        print(False)
    if (ord(char)>47 and ord(char)<58) and done==True:
        print(True)
        done=False
    else:
        print(False)
    if  (ord(char)>96 and ord(char)<123) and d1one==True:
        print(True)
        d1one=False
    else:
        print(False)
    if (ord(char)>64 and ord(char)<91) and d2one==True:
        print(True)
        d2one=False
    else:
        print(False)
   