import math
s=input()

keys={"1": {"x":8.25,"y":46.25},
      "2": {"x":27.25,"y":46.25},
      "3": {"x":46.25,"y":46.25},
      "4": {"x":65.25,"y":46.25},
      "5": {"x":84.25,"y":46.25},
      "6": {"x":103.25,"y":46.25},
      "7": {"x":122.25,"y":46.25},
      "8": {"x":141.25,"y":46.25},
      #row2
      "q": {"x":8.25,"y":27.25},
      "w": {"x":27.25,"y":27.25},
      "e": {"x":46.25,"y":27.25},
      "r": {"x":65.25,"y":27.25},
      "t": {"x":84.25,"y":27.25},
      "y": {"x":103.25,"y":27.25},
      "u": {"x":122.25,"y":27.25},
      "i": {"x":141.25,"y":27.25},
      #r3
      "a": {"x":8.25,"y":8.25},
      "s": {"x":27.25,"y":8.25},
      "d": {"x":46.25,"y":8.25},
      "f": {"x":65.25,"y":8.25},
      "g": {"x":84.25,"y":8.25},
      "h": {"x":103.25,"y":8.25},
      "j": {"x":122.25,"y":8.25},
      "k": {"x":141.25,"y":8.25}
}
lm = {"name": "left middle",  "data": keys["a"]}
li = {"name": "left index",   "data": keys["s"]}
ri = {"name": "right index",  "data": keys["j"]}
rm = {"name": "right middle", "data": keys["k"]}
fingers=[lm,li,ri,rm]
def move(char):
    if char in keys:
        l=[]
        for finger in fingers:
    
            dist=math.hypot(finger["data"]["x"]-keys[char]["x"],finger["data"]["y"]-keys[char]["y"])
            l.append((finger,dist))
        m = sorted(l, key=lambda item: item[1])
        cf = m[0][0]
        cf["data"]=keys[char]
        print(f"{char} was pressed by {cf["name"]}")
    else:
        print("not on keyboard")

for ch in s:
    move(ch)
        
            
