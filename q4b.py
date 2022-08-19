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

cen=pd.read_excel("dataset/census.xlsx")
cen2=cen[["Level","State","TRU","TOT_P"]]

l1=[]

l1.append([cen2["State"][0],cen2["TOT_P"][0]])
for i in range(3,len(cen2)):
    if(cen2["Level"][i]=="STATE" and cen2["TRU"][i]=="Total"):
        l1.append([cen2["State"][i],cen2["TOT_P"][i]])

df1=pd.DataFrame(l1)

df1["ratio"]=d3[1]/df1[1]
df1[0]=d3[0]
df2=df1.iloc[1:]
df2=df2.sort_values("ratio").reset_index(drop="True")
l4=[]

l4.append([df2.iloc[-1][0],df2.iloc[-1]["ratio"]])
l4.append([df2.iloc[-2][0],df2.iloc[-2]["ratio"]])
l4.append([df2.iloc[-3][0],df2.iloc[-3]["ratio"]])
l4.append([df2.iloc[0][0],df2.iloc[0]["ratio"]])
l4.append([df2.iloc[1][0],df2.iloc[1]["ratio"]])
l4.append([df2.iloc[2][0],df2.iloc[2]["ratio"]])

df3=pd.DataFrame(l4)
df3.columns=["state-code","ratio"]

#d5.to_csv("3-to-2-ratio.csv", index=False)
df3.to_csv("2-to-1-ratio.csv", index=False)
