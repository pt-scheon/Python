import requests
import json 
import csv

url= "https://jsonplaceholder.typicode.com/users/1"
response=requests.get(url)
data=response.json()
print(data)
for key,value in data.items():
    print(key,value,end="\n \n")



with open("objects.json","r") as f:
    readr=json.load(f)
    for item in readr:
        shape = item["object"]
        sides = item["sides"]
        area = item["area"]
        
        print(f"The area of {shape} with {sides} sides is {area} ")


with open("price.csv","r") as g:
    csvReadr=csv.DictReader(g,delimiter=",")

    # for d in csvReadr:
    #     print(f"{d["Object"]} is bought at price of {int(d["Buying Price"])} and sold at price of {int(d["Selling Price"])} making profit of {int(d["Selling Price"])-int(d["Buying Price"])}$")
    with open("newprice.csv","w") as write:
        l=["Object","Buying Price","Selling Price"]
        csvwriter=csv.DictWriter(write,delimiter=" ",fieldnames=l)
        for d in csvReadr:
            csvwriter.writerow(d)