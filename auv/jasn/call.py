file = open("commands.csv", "r")
content = file.read()
file.close()

lines = content.splitlines()

for line in lines[1:]:
  parts = line.split(",")
  for part in parts:
    action = part.strip().replace('"', "").lower()
    filename = action + ".py"
    exec(open(filename).read())
