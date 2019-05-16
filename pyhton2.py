import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

msft = pd.read_csv("tips.csv")

msft['Split the bill equaly'] =msft["total_bill"] / msft["size"]
msft['Bill excluding tip'] =msft["total_bill"] - msft["tip"]

booleans =[]
for roker in msft["smoker"]:
    if roker =="Yes":
        booleans.append(True)
    else:
        booleans.append(False)

isnroker=pd.Series(booleans)
msft[isnroker]
print("The dataframe filtered by smokers: ")
print (msft[isnroker].head(50))

print("The correlation cofficient of the total bills & the tips shown in the above dataframe is: ")

print(msft['total_bill'].corr(msft['tip']))


fig = plt.figure()
fig.patch.set_facecolor("lightgrey")

graph1 = fig.add_subplot(2,2,1,facecolor="#E1F5FE")
graph1.scatter(msft["sex"],msft["total_bill"],label="scatter point",color="#01579B")
graph1.set_title("Who pays more?")

plt.legend()
plt.xlabel("Gender", color="#01579B")
plt.ylabel("Total Bill", color="#01579B")
msft=msft.sort_values('total_bill')

graph2= fig.add_subplot(2,2,2, facecolor="#01579B")
graph2.bar(msft["sex"],msft["tip"], label = "bar graph", facecolor="#E1F5FE")
graph2.set_title("Who gives more tip?")


plt.legend()
plt.xlabel("Gender", color="#01579B")
plt.ylabel("Tip given", color="#01579B")

plt.show()
