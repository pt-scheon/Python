import csv
with open("price.csv") as f:
    reader=csv.reader(f)
    rows=list(reader)
    col=len(rows[0])
    length=[]
    for i in range(col):
        len2=0
        for row in rows:
            if len(row[i])>len2:
                len2=len(row[i])
        length.append(len2)

with open("price2.csv","w") as prt:
    for r in rows:
        newro=[r[i].ljust(length[i]) for i in range(col)]
        prt.write(" ".join(newro)+"\n")

