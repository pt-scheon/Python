n = int(input())
marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores
query_name = input()
for key,value in marks.items():
    if key == query_name:
        p=(value[0]+value[2]+value[1])/3
        print(f"{p:.2f}")
