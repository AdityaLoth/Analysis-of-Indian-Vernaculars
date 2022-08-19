import pandas as pd
import numpy as np

cen=pd.read_excel("dataset/DDW-0000C-08.xlsx")
cen=cen[6:].reset_index(drop="True")

cen2=cen[cen[cen.columns[5]]=="All ages"]
cen2=cen2[cen[cen.columns[4]]=="Total"].reset_index(drop="True")

l1=[]

for i in cen2.itertuples():
    l1.append([i[2] ,i[11],i[12]])
    l1.append([i[2], i[14]+i[17]+i[44], i[15]+i[18]+i[45]])
    l1.append([i[2], i[20],i[21]])
    l1.append([i[2], i[23],i[24]])
    l1.append([i[2], i[26],i[27]])
    l1.append([i[2], i[29]+i[32]+i[35]+i[38],i[30]+i[33]+i[36]+i[39]])
    l1.append([i[2], i[41],i[42]])

df1=pd.DataFrame(l1)

data2=pd.read_excel("dataset/DDW-C19-0000.xlsx")
data2=data2[5:].reset_index(drop="True")
df2=data2[data2.columns[[0,3,4,6,7,9,10]]]
df2=df2[df2[df2.columns[1]]=="Total"]
df2=df2[df2[df2.columns[2]]!="Total"].reset_index(drop="True")

df2.columns=["state/ut","a","literacy-group","m2","f2","m3","f3"]
df2["m1"]=(df1[1]-df2["m2"])/df1[1]
df2["m2"]=(df2["m2"]-df2["m3"])/df1[1]
df2["f1"]=(df1[2]-df2["f2"])/df1[2]
df2["f2"]=(df2["f2"]-df2["f3"])/df1[2]
df2["m3"]=df2["m3"]/df1[1]
df2["f3"]=df2["f3"]/df1[2]

idx=df2.groupby(["state/ut"])["m2"].transform("max")==df2["m2"]
m2=df2[idx].reset_index(drop="True")
idx=df2.groupby(["state/ut"])["m1"].transform("max")==df2["m1"]
m1=df2[idx].reset_index(drop="True")
idx=df2.groupby(["state/ut"])["m3"].transform("max")==df2["m3"]
m3=df2[idx].reset_index(drop="True")

idx=df2.groupby(["state/ut"])["f1"].transform("max")==df2["f1"]
f1=df2[idx].reset_index(drop="True")
idx=df2.groupby(["state/ut"])["f2"].transform("max")==df2["f2"]
f2=df2[idx].reset_index(drop="True")
idx=df2.groupby(["state/ut"])["f3"].transform("max")==df2["f3"]
f3=df2[idx].reset_index(drop="True")

out1=m1[["state/ut","literacy-group","m1"]]
out1.columns=["state/ut","literacy-group-males","ratio-males"]
out1["literacy-group-females"]=f1["literacy-group"]
out1["ratio-females"]=f1["f1"]

out2=m2[["state/ut","literacy-group","m2"]]
out2.columns=["state/ut","literacy-group-males","ratio-males"]
out2["literacy-group-females"]=f2["literacy-group"]
out2["ratio-females"]=f2["f2"]

out3=m3[["state/ut","literacy-group","m3"]]
out3.columns=["state/ut","literacy-group-males","ratio-males"]
out3["literacy-group-females"]=f3["literacy-group"]
out3["ratio-females"]=f3["f3"]

out3.to_csv("literacy-gender-a.csv",index=False)
out2.to_csv("literacy-gender-b.csv",index=False)
out1.to_csv("literacy-gender-c.csv",index=False)
