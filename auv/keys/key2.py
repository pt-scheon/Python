import math
st=input()
# Reference Point: fn key bottom-left corner is (0.0, 0.0)
# Format: "Key": ((x1, y1), (x1, y2), (x2, y1), (x2, y2))
# Where x1/y1 = bottom-left, x2/y2 = top-right
# Reference Point: fn key bottom-left corner is (0.0, 0.0)
# Format: "Key": {"row": int, "col": int, "coords": ((x1, y1), (x1, y2), (x2, y1), (x2, y2))}
# Where x1/y1 = bottom-left, x2/y2 = top-right

# Reference Point: fn key bottom-left corner is (0.0, 0.0)
# Format: "character": {"key": "character", "row": int, "col": int, "coords": ((x1, y1), (x1, y2), (x2, y1), (x2, y2))}
keys = {
    # ---------------------------------------------------------
    # ROW 1: NUMBER ROW (1 -> 8)   [y1: 38.0, y2: 54.5]
    # ---------------------------------------------------------
    "1": {"key": "1", "row": 1, "col": 1, "coords": ((0.0, 38.0), (0.0, 54.5), (16.5, 54.5), (16.5, 38.0))},
    "2": {"key": "2", "row": 1, "col": 2, "coords": ((19.0, 38.0), (19.0, 54.5), (35.5, 54.5), (35.5, 38.0))},
    "3": {"key": "3", "row": 1, "col": 3, "coords": ((38.0, 38.0), (38.0, 54.5), (54.5, 54.5), (54.5, 38.0))},
    "4": {"key": "4", "row": 1, "col": 4, "coords": ((57.0, 38.0), (57.0, 54.5), (73.5, 54.5), (73.5, 38.0))},
    "5": {"key": "5", "row": 1, "col": 5, "coords": ((76.0, 38.0), (76.0, 54.5), (92.5, 54.5), (92.5, 38.0))},
    "6": {"key": "6", "row": 1, "col": 6, "coords": ((95.0, 38.0), (95.0, 54.5), (111.5, 54.5), (111.5, 38.0))},
    "7": {"key": "7", "row": 1, "col": 7, "coords": ((114.0, 38.0), (114.0, 54.5), (130.5, 54.5), (130.5, 38.0))},
    "8": {"key": "8", "row": 1, "col": 8, "coords": ((133.0, 38.0), (133.0, 54.5), (149.5, 54.5), (149.5, 38.0))},

    # ---------------------------------------------------------
    # ROW 2: TOP LETTER ROW (Q -> I)  [y1: 19.0, y2: 35.5]
    # ---------------------------------------------------------
    "q": {"key": "q", "row": 2, "col": 1, "coords": ((0.0, 19.0), (0.0, 35.5), (16.5, 35.5), (16.5, 19.0))},
    "w": {"key": "w", "row": 2, "col": 2, "coords": ((19.0, 19.0), (19.0, 35.5), (35.5, 35.5), (35.5, 19.0))},
    "e": {"key": "e", "row": 2, "col": 3, "coords": ((38.0, 19.0), (38.0, 35.5), (54.5, 35.5), (54.5, 19.0))},
    "r": {"key": "r", "row": 2, "col": 4, "coords": ((57.0, 19.0), (57.0, 35.5), (73.5, 35.5), (73.5, 19.0))},
    "t": {"key": "t", "row": 2, "col": 5, "coords": ((76.0, 19.0), (76.0, 35.5), (92.5, 35.5), (92.5, 19.0))},
    "y": {"key": "y", "row": 2, "col": 6, "coords": ((95.0, 19.0), (95.0, 35.5), (111.5, 35.5), (111.5, 19.0))},
    "u": {"key": "u", "row": 2, "col": 7, "coords": ((114.0, 19.0), (114.0, 35.5), (130.5, 35.5), (130.5, 19.0))},
    "i": {"key": "i", "row": 2, "col": 8, "coords": ((133.0, 19.0), (133.0, 35.5), (149.5, 35.5), (149.5, 19.0))},

    # ---------------------------------------------------------
    # ROW 3: HOME ROW (A -> K)  [y1: 0.0, y2: 16.5]
    # ---------------------------------------------------------
    "a": {"key": "a", "row": 3, "col": 1, "coords": ((0.0, 0.0), (0.0, 16.5), (16.5, 16.5), (16.5, 0.0))},
    "s": {"key": "s", "row": 3, "col": 2, "coords": ((19.0, 0.0), (19.0, 16.5), (35.5, 16.5), (35.5, 0.0))},
    "d": {"key": "d", "row": 3, "col": 3, "coords": ((38.0, 0.0), (38.0, 16.5), (54.5, 16.5), (54.5, 0.0))},
    "f": {"key": "f", "row": 3, "col": 4, "coords": ((57.0, 0.0), (57.0, 16.5), (73.5, 16.5), (73.5, 0.0))},
    "g": {"key": "g", "row": 3, "col": 5, "coords": ((76.0, 0.0), (76.0, 16.5), (92.5, 16.5), (92.5, 0.0))},
    "h": {"key": "h", "row": 3, "col": 6, "coords": ((95.0, 0.0), (95.0, 16.5), (111.5, 16.5), (111.5, 0.0))},
    "j": {"key": "j", "row": 3, "col": 7, "coords": ((114.0, 0.0), (114.0, 16.5), (130.5, 16.5), (130.5, 0.0))},
    "k": {"key": "k", "row": 3, "col": 8, "coords": ((133.0, 0.0), (133.0, 16.5), (149.5, 16.5), (149.5, 0.0))},
}


lm = {"name": "left middle",  "data": keys["a"]}
li = {"name": "left index",   "data": keys["s"]}
ri = {"name": "right index",  "data": keys["j"]}
rm = {"name": "right middle", "data": keys["k"]}


fingers = [lm, li, ri, rm]
val=[]

def press(character,finger):
    print(f"{character} pressed by {finger['name']}")

def move(char):
    if char in keys:
        temp_distf = []
        for finger in fingers:
            if keys[char]["col"]>finger["data"]["col"] and keys[char]["row"]>=finger["data"]["row"]:

                dist = math.hypot(keys[char]["coords"][1][0]-finger["data"]["coords"][3][0], 
                                  keys[char]["coords"][1][1]-finger["data"]["coords"][3][1])
            #different row but same column
            elif keys[char]["col"] <= finger["data"]["col"] and keys[char]["row"]>finger["data"]["row"]:
                dist = math.hypot(keys[char]["coords"][2][0]-finger["data"]["coords"][0][0], 
                                  keys[char]["coords"][2][1]-finger["data"]["coords"][0][1])
            elif keys[char]["col"] < finger["data"]["col"] and keys[char]["row"]<=finger["data"]["row"]:
                dist = math.hypot(keys[char]["coords"][3][0]-finger["data"]["coords"][1][0], 
                                  keys[char]["coords"][3][1]-finger["data"]["coords"][1][1])
            else:
                dist = math.hypot(keys[char]["coords"][0][0]-finger["data"]["coords"][2][0], 
                                  keys[char]["coords"][0][1]-finger["data"]["coords"][2][1])
             
            temp_distf.append((finger, dist))
            
        sorted_distf = sorted(temp_distf, key=lambda item: item[1])
        closest_finger = sorted_distf[0][0]
        initial_pos = closest_finger["data"]["key"]
        closest_finger["data"] = keys[char]
        final_pos = closest_finger["data"]["key"]
        
        val.append({
            "finger_obj": closest_finger,
            "message": f"Moved from '{initial_pos}' to '{final_pos}' to type '{char}'."
        })
        press(char, closest_finger)
    else:
        print("not on keyboard")


for ch in st:
    move(ch)




















                      
# def vertical_shift():
# Letters
# a = "A"
# b = "B"
# c = "C"
# d = "D"
# e = "E"
# f = "F"
# g = "G"
# h = "H"
# i = "I"
# j = "J"
# k = "K"
# l = "L"
# m = "M"
# n = "N"
# o = "O"
# p = "P"
# q = "Q"
# r = "R"
# s = "S"
# t = "T"
# u = "U"
# v = "V"
# w = "W"
# x = "X"
# y = "Y"
# z = "Z"

# # Numbers & Top Row Symbols
# num_1 = "1 !"
# num_2 = "2 @"
# num_3 = "3 #"
# num_4 = "4 $"
# num_5 = "5 %"
# num_6 = "6 ^"
# num_7 = "7 &"
# num_8 = "8 *"
# num_9 = "9 ("
# num_0 = "0 )"

# # Punctuation & Symbols
# tilde = "` ~"
# minus = "- _"
# equals = "= +"
# bracket_left = "[ {"
# bracket_right = "] }"
# backslash = "\\ |"
# semicolon = "; :"
# quote = "' \""
# comma = ", <"
# period = ". >"
# slash = "/ ?"

# # Modifiers & System Keys
# esc = "esc"
# tab = "tab"
# caps_lock = "caps lock"
# shift_left = "shift"
# shift_right = "shift"
# fn = "fn 🌐"
# ctrl = "control ⌃"
# opt_left = "option ⌥"
# opt_right = "option ⌥"
# cmd_left = "command ⌘"
# cmd_right = "command ⌘"
# space = "spacebar"
# return_key = "return"
# delete = "delete"

# # Navigation
# arrow_up = "▲"
# arrow_down = "▼"
# arrow_left = "◀"
# arrow_right = "▶"

# # Function Row / Media Keys
# f1 = "F1"
# f2 = "F2"
# f3 = "F3"
# f4 = "F4"
# f5 = "F5"
# f6 = "F6"
# f7 = "F7"
# f8 = "F8"
# f9 = "F9"
# f10 = "F10"
# f11 = "F11"
# f12 = "F12"
# touch_id = "Touch ID"
# k=input()
# if k=="esc" or "~" or "1" or "2" or "tab" or "caps lock" or "shift" or "fn" or "left control" or "left option" or "z" or "q":
#     print(a)
#     if k=="a":
#         print("dont lift hand")
# elif (k=="w" or "x" or "left command" or "3" or "s"):
#     print(b)
#     if k=="s":
#         print("dont lift finger")
# elif k=="e" or "c"
   