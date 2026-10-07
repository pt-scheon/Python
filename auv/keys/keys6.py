import math

s = input()

keys = {
    "1": {"x": 8.25, "y": 46.25},
    "2": {"x": 27.25, "y": 46.25},
    "3": {"x": 46.25, "y": 46.25},
    "4": {"x": 65.25, "y": 46.25},
    "5": {"x": 84.25, "y": 46.25},
    "6": {"x": 103.25, "y": 46.25},
    "7": {"x": 122.25, "y": 46.25},
    "8": {"x": 141.25, "y": 46.25},
    # row2
    "q": {"x": 8.25, "y": 27.25},
    "w": {"x": 27.25, "y": 27.25},
    "e": {"x": 46.25, "y": 27.25},
    "r": {"x": 65.25, "y": 27.25},
    "t": {"x": 84.25, "y": 27.25},
    "y": {"x": 103.25, "y": 27.25},
    "u": {"x": 122.25, "y": 27.25},
    "i": {"x": 141.25, "y": 27.25},
    # r3
    "a": {"x": 8.25, "y": 8.25},
    "s": {"x": 27.25, "y": 8.25},
    "d": {"x": 46.25, "y": 8.25},
    "f": {"x": 65.25, "y": 8.25},
    "g": {"x": 84.25, "y": 8.25},
    "h": {"x": 103.25, "y": 8.25},
    "j": {"x": 122.25, "y": 8.25},
    "k": {"x": 141.25, "y": 8.25},
}

fingers = [
    {"name": "left middle", "data": keys["a"]},
    {"name": "left index", "data": keys["s"]},
    {"name": "right index", "data": keys["j"]},
    {"name": "right middle", "data": keys["k"]},
]


def get_dist(p1, p2):
  return math.hypot(p1["x"] - p2["x"], p1["y"] - p2["y"])


i = 0
while i < len(s):
  char1 = s[i]
  if char1 not in keys:
    print(f"'{char1}' not on keyboard")
    i += 1
    continue

  next_char = s[i + 1] if i + 1 < len(s) and s[i + 1] in keys else None

  best1f = None
  minC = float("inf")
  for f in fingers:
    cost = get_dist(f["data"], keys[char1])
    if cost < minC:
      minC = cost
      best1f = f

  bestPair = None
  minDC = float("inf")

  if next_char and next_char != char1:
    char2 = next_char
    for f1_idx, sub_f1 in enumerate(fingers):
      for f2_idx, sub_f2 in enumerate(fingers):
        if f1_idx == f2_idx:
          continue
       
        cost = max(
            get_dist(sub_f1["data"], keys[char1]),
            get_dist(sub_f2["data"], keys[char2]),
        )
        if cost < minDC:
          minDC = cost
          bestPair = (sub_f1, sub_f2)
  if next_char and next_char != char1 and bestPair and minDC <= minC:
    bestPair[0]["data"] = keys[char1]
    bestPair[1]["data"] = keys[char2]
    print(
        f"'{char1}' by {bestPair[0]['name']} & '{char2}' by {bestPair[1]['name']} were pressed together"
    )
    i += 2
  else:
    best1f["data"] = keys[char1]
    print(f"'{char1}' was pressed by {best1f['name']}")
    i += 1