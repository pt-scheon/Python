import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gas=pd.read_csv("gp.csv")
print(gas)
plt.figure(figsize=(8,5),dpi=200)
plt.title("Gas prices over time (in USD)")
for country in gas:
    if country!="Year":
        plt.plot(gas.Year,gas[country],marker=".")
print(gas.Year[::3])
plt.xticks(gas.Year[::3])
plt.xlabel("Year")
plt.ylabel("Price (in USD)")
plt.show()