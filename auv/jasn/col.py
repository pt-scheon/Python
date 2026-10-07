import csv
fields = ["Object", "Buying Price", "Selling Price"]

with open("price.csv") as f:
    rows = list(csv.DictReader(f))
w = {}
for k in fields:
    w[k] = len(k)
for r in rows:
    for k, v in r.items():
        w[k] = max(w[k], len(v))
with open("newprice.csv", "w") as f:
    header = []
    for k in fields:
        header.append(f"{k:<{w[k]}}")
    f.write("  ".join(header) + "\n")

    for r in rows:
        ro = []
        for k in fields:
            ro.append(f"{r[k]:<{w[k]}}")
        f.write("  ".join(ro) + "\n")
