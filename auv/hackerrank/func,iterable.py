N = int(input())
a=[]
for _ in range(N):
    func, *line = input().split()
    if func=="insert":
        c=int(line[0])
        d=int(line[1])
        a.insert(c,d)
    elif func=="append":
        b=int(line[0])
        a.append(b)
    elif func=="reverse":
        a.reverse()
    elif func=="sort":
        a.sort()
    elif func=="pop":
        a.pop()
    elif func=="remove":
        c=int(line[0])
        a.remove(c)
    elif func=="print":
        print(a)


