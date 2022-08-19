import numpy as np
import pandas as pd

data=pd.read_excel("dataset/DDW-C18-0000.xlsx")
data=data[5:].reset_index(drop="True")
twolang=data[data.columns[[0,3,4,6,7,9,10]]]

twolang.columns=["Area","pop","age","2male","2female","3male","3female"]
twolang["2male"]=twolang["2male"]-twolang["3male"]
twolang["2female"]=twolang["2female"]-twolang["3female"]

cen=pd.read_excel("dataset/DDW-0000C-14.xlsx")

cen=cen[6:].reset_index(drop="True")
cen2=cen[cen.columns[[1,4,6,7]]]
cen2.columns=["area","age","totmale","totfemale"]

l1=[]

for i in range(0,len(cen2),19):
    
    l1.append([cen2["area"][i+1],'5-9',cen2["totmale"][i+2],cen2["totfemale"][i+2]])
    l1.append([cen2["area"][i+1],'10-14',cen2["totmale"][i+3],cen2["totfemale"][i+3]])
    l1.append([cen2["area"][i+1],'15-19',cen2["totmale"][i+4],cen2["totfemale"][i+4]])
    l1.append([cen2["area"][i+1],'20-24',cen2["totmale"][i+5],cen2["totfemale"][i+5]])
    l1.append([cen2["area"][i+1],'25-29',cen2["totmale"][i+6],cen2["totfemale"][i+6]])
    l1.append([cen2["area"][i+1],'30-49',cen2["totmale"][i+7]+cen2["totmale"][i+8]+cen2["totmale"][i+9]+cen2["totmale"][i+10],cen2["totfemale"][i+7]+cen2["totfemale"][i+8]+cen2["totfemale"][i+9]+cen2["totfemale"][i+10]])
    l1.append([cen2["area"][i+1],'50-69',cen2["totmale"][i+11]+cen2["totmale"][i+12]+cen2["totmale"][i+13]+cen2["totmale"][i+14],cen2["totfemale"][i+11]+cen2["totfemale"][i+12]+cen2["totfemale"][i+13]+cen2["totfemale"][i+14]])
    l1.append([cen2["area"][i+1],'70+',cen2["totmale"][i+15]+cen2["totmale"][i+16]+cen2["totmale"][i+17],cen2["totfemale"][i+15]+cen2["totfemale"][i+16]+cen2["totfemale"][i+17]])
    #l1.append([cen2["area"][i+1],'Age not stated',cen2["totmale"][i+18],cen2["totfemale"][i+18]])


df1=pd.DataFrame(l1)

twolang=twolang[twolang["pop"]=="Total"]
twolang=twolang[twolang["age"]!="Age not stated"]
twolang=twolang[twolang["age"]!="Total"].reset_index(drop="True")

df1.columns=["area","age","totmale","totfemale"]

df2=df1[["area","age"]]
df2["1male"]=df1["totmale"]-twolang["2male"]-twolang["3male"]
df2["1female"]=df1["totfemale"]-twolang["2female"]-twolang["3female"]

lang1m=df2[["area","age","1male"]]
lang1f=df2[["area","age","1female"]]
lang1m["ratio"]=lang1m["1male"]/df1["totmale"]
lang1f["ratio"]=lang1f["1female"]/df1["totfemale"]

idx=lang1m.groupby(["area"])["ratio"].transform("max")==lang1m["ratio"]
lang1m=lang1m[idx].reset_index(drop="True")
idx=lang1f.groupby(["area"])["ratio"].transform("max")==lang1f["ratio"]
lang1f=lang1f[idx].reset_index(drop="True")

lang2m=twolang[["Area","age","2male"]]
lang2f=twolang[["Area","age","2female"]]
lang2m["ratio"]=lang2m["2male"]/df1["totmale"]
lang2f["ratio"]=lang2f["2female"]/df1["totfemale"]

idx=lang2m.groupby(["Area"])["ratio"].transform("max")==lang2m["ratio"]
lang2m=lang2m[idx].reset_index(drop="True")
idx=lang2f.groupby(["Area"])["ratio"].transform("max")==lang2f["ratio"]
lang2f=lang2f[idx].reset_index(drop="True")

lang3m=twolang[["Area","age","3male"]]
lang3f=twolang[["Area","age","3female"]]
lang3m["ratio"]=lang3m["3male"]/df1["totmale"]
lang3f["ratio"]=lang3f["3female"]/df1["totfemale"]

idx=lang3m.groupby(["Area"])["ratio"].transform("max")==lang3m["ratio"]
lang3m=lang3m[idx].reset_index(drop="True")
idx=lang3f.groupby(["Area"])["ratio"].transform("max")==lang3f["ratio"]
lang3f=lang3f[idx].reset_index(drop="True")

out1=lang1m[["area","age","ratio"]]
out1.columns=["state/ut","age-group-males","ratio-males"]
out1["age-group-females"]=lang1f["age"]
out1["ratio-females"]=lang1f["ratio"]

out2=lang2m[["Area","age","ratio"]]
out2.columns=["state/ut","age-group-males","ratio-males"]
out2["age-group-females"]=lang2f["age"]
out2["ratio-females"]=lang2f["ratio"]

out3=lang3m[["Area","age","ratio"]]
out3.columns=["state/ut","age-group-males","ratio-males"]
out3["age-group-females"]=lang3f["age"]
out3["ratio-females"]=lang3f["ratio"]

out3.to_csv("age-gender-a.csv",index=False)
out2.to_csv("age-gender-b.csv",index=False)
out1.to_csv("age-gender-c.csv",index=False)
