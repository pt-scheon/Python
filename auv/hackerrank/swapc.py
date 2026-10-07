n =input()
s = ""
for char in n:
    if char>="A" and char<="Z":
        char =chr(ord(char)+32)
        s =s+char

    elif char >= "a" and char <= "z":
        char = chr(ord(char)-32)
        s =s+char

print(s)
