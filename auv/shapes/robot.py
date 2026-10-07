import math
g=18
hands="|"+" "*15+"|"
for i in range(60):
    #hair
    if i==0:
        print(" "*16+30*"-")
    elif i==2:
        print(" "*15+"|"+" "*7+"."+" "+"."+" "*10+"."+" "+"."+" "*7+"|")
    elif i==3:
        print(" "*15+"|"+" "*6+"."+" "*3+"."+" "*8+"."+" "*3+"."+" "*6+"|")
    elif i==4:
        print(" "*15+"|"+" "*7+"."+" "+"."+" "*10+"."+" "+"."+" "*7+"|")
    elif i==6:
        print(" "*15+"|"+" "*8+"."+" "*12+"."+" "*8+"|")
    elif i==7:
        print(" "*15+"|"+" "*9+"."+" "*9+"."+" "*10+"|")
    elif i==8:
        print(" "*15+"|"+" "*11+"."+" "*2+"."+" "*2+"."+" "*12+"|")
    #left face and right face
    elif i<10 and i>4:
        print(" "*15+"|"+" "*30+"|")
        #cjaw
    elif i==20:
        print(" "*16+30*"-")
        #neck
    elif i>20 and i<25:
        print(" "*26+"|"+" "*10+"|")
        #chestline
    elif i==25:
        print(" "+"-"*61)
        #shoulder
    elif i>25 and i<28:
        print("|"+" "*62+"|")
        #hands
    elif i>35 and i<45:
        print(hands+" "*30+hands)
    elif i==28:
        print(hands+" "*14+"."*2+" "*14+hands)
    elif i==29:
        print(hands+" "*12+"."+" "*4+"."+" "*12+hands)
    elif i==30:
        print(hands+" "*11+"."+" "*6+"."+" "*11+hands)
    elif i==31:
        print(hands+" "*10+"."+"."*8+"."+" "*10+hands)
    elif i==32:
        print(hands+" "*9+"."+" "*10+"."+" "*9+hands)
    elif i==33:
        print(hands+" "*8+"."+" "*12+"."+" "*8+hands)
    elif i==34:
        print(hands+" "*7+"."+" "*14+"."+" "*7+hands)
 #waist
    elif i==45:
        print(" "+"-"*61)
    elif i>45:
        print(" "*20+"|"+" "*8+"|"+" "*2+"|"+" "*8+"|")
    elif i==59:
        print(" "*21+"-"*22)





