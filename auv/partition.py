import itertools
m=int(input())
l=set()

def product(n):
    ranges=[range(n)]*n
    for combination in itertools.product(*ranges):
        if sum(combination)==n:
            l.add(tuple(sorted(combination)))
    l.add(m)
    return l
print(product(m))
print(len(l))

