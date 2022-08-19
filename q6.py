import numpy as np
import pandas as pd

cen=pd.read_excel("dataset/DDW-0000C-08.xlsx")
cen=cen[6:].reset_index(drop="True")
cen2=cen[cen[cen.columns[5]]=="All ages"]
cen2=cen2[cen[cen.columns[4]]=="Total"].reset_index(drop="True")

l1=[]

for i in cen2.itertuples():
    l1.append([i[2] ,i[10]])
    l1.append([i[2], i[13]+i[16]+i[43]])
    l1.append([i[2], i[19]])
    l1.append([i[2], i[22]])
    l1.append([i[2], i[25]])
    l1.append([i[2], i[28]+i[31]+i[34]+i[37]])
    l1.append([i[2], i[40]])

df1=pd.DataFrame(l1)

data2=pd.read_excel("dataset/DDW-C19-0000.xlsx")
data2=data2[5:].reset_index(drop="True")
df2=data2[data2.columns[[0,3,4,8]]]
df2=df2[df2[df2.columns[1]]=="Total"]
df2=df2[df2[df2.columns[2]]!="Total"].reset_index(drop="True")

df2["perc"]=(df2[df2.columns[3]]/df1[1])*100
df2.columns=["state/ut","a","literacy-group","b","percentage"]
df2=df2[["state/ut","literacy-group","percentage"]]
idx=df2.groupby(["state/ut"])["percentage"].transform("max")==df2["percentage"]
data2=df2[idx].reset_index(drop="True")

data2.to_csv("literacy-india.csv",index=False)


