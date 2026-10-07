s = input()
result = ""
capitalize=False

for char in s:
    if char == "_":
        capitalize=True
    elif capitalize==True:
        result+=char.upper()
        capitalize=False
    else:
        result+=char

print(result)