import numpy as np
import pandas as pd

data=pd.read_excel("dataset/DDW-C18-0000.xlsx")
data=data[5:].reset_index(drop="True")
newd=data[data.columns[[0,3,4,8]]]
newd.columns=["Area","pop","age","count"]
newd=newd[newd["age"]!="Age not stated"]

cen=pd.read_excel("dataset/DDW-0000C-14.xlsx")
cen=cen[6:].reset_index(drop="True")
cen2=cen[cen.columns[[1,4,5]]]
cen2.columns=["area","age","num"]

l1=[]

for i in range(0,len(cen2),19):
    
    l1.append([cen2["area"][i+1],'5-9',cen2["num"][i+2]])
    l1.append([cen2["area"][i+1],'10-14',cen2["num"][i+3]])
    l1.append([cen2["area"][i+1],'15-19',cen2["num"][i+4]])
    l1.append([cen2["area"][i+1],'20-24',cen2["num"][i+5]])
    l1.append([cen2["area"][i+1],'25-29',cen2["num"][i+6]])
    l1.append([cen2["area"][i+1],'30-49',cen2["num"][i+7]+cen2["num"][i+8]+cen2["num"][i+9]+cen2["num"][i+10]])
    l1.append([cen2["area"][i+1],'50-69',cen2["num"][i+11]+cen2["num"][i+12]+cen2["num"][i+13]+cen2["num"][i+14]])
    l1.append([cen2["area"][i+1],'70+',cen2["num"][i+15]+cen2["num"][i+16]+cen2["num"][i+17]])
   # l1.append([cen2["area"][i+1],'Age not stated',cen2["num"][i+18]])


df1=pd.DataFrame(l1)

newd=newd[newd["pop"]=="Total"]
newd=newd[newd["age"]!="Total"].reset_index(drop="True")

newd["total"]=df1[2]
newd["percentage"]=(newd["count"]/newd["total"])*100
idx=newd.groupby(["Area"])["percentage"].transform("max")==newd["percentage"]
data2=newd[idx].reset_index(drop="True")
data2=data2[['Area','age','percentage']]
data2.columns=["state/ut", "age-group", "percentage"]

data2.to_csv("age-india.csv",index=False)

