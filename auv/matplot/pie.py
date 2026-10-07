import matplotlib.pyplot as plt
import numpy as np
import csv 
ages=[]
populations=[]
with open("population.csv","r") as p:
    ppl=csv.DictReader(p)
    for i in ppl:
        ages.append(i["Age_Range"])
        populations.append(int(i["Population"]))
plt.plot(ages,populations)
plt.xlabel("Age Range")
plt.ylabel("Population")
plt.title("Population by Age")

plt.show()