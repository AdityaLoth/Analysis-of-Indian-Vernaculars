import numpy as np
import pandas as pd

d1=pd.read_excel("dataset/DDW-C19-0000.xlsx")
d2=d1[5:][d1[5:].columns[[0,3,4,5,8]]].reset_index(drop=True)
d2.columns=["area","x","y","two","three"]
l2=[]
for i in range(len(d2)):
    if(d2["x"][i]=="Total" and d2["y"][i]=="Total"):
        l2.append([d2["area"][i], d2["two"][i],d2["three"][i]])
        
d3=pd.DataFrame(l2)
d3["ratio"]=d3[2]/d3[1]



d4=d3.iloc[1:]
d4=d4.sort_values("ratio").reset_index(drop="True")

l3=[]

l3.append([d4.iloc[-1][0],d4.iloc[-1]["ratio"]])
l3.append([d4.iloc[-2][0],d4.iloc[-2]["ratio"]])
l3.append([d4.iloc[-3][0],d4.iloc[-3]["ratio"]])
l3.append([d4.iloc[0][0],d4.iloc[0]["ratio"]])
l3.append([d4.iloc[1][0],d4.iloc[1]["ratio"]])
l3.append([d4.iloc[2][0],d4.iloc[2]["ratio"]])

d5=pd.DataFrame(l3)
d5.columns=["state-code","ratio"]
d5.to_csv("3-to-2-ratio.csv", index=False)

