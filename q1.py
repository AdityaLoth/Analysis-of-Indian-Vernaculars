import numpy as np
import pandas as pd

cen=pd.read_excel("dataset/census.xlsx")
d1=pd.read_excel("dataset/DDW-C19-0000.xlsx")

cen2=cen[["Level","State","TRU","TOT_P"]]

l1=[]
l1.append([cen2["State"][0],cen2["TOT_P"][0]])
for i in range(3,len(cen2)):
    if(cen2["Level"][i]=="STATE" and cen2["TRU"][i]=="Total"):
        l1.append([cen2["State"][i],cen2["TOT_P"][i]])

d2=d1[5:][d1[5:].columns[[2,3,4,5,8]]].reset_index(drop=True)
d2.columns=["area","x","y","sec","thr"]

l2=[]
for i in range(len(d2)):
    if(d2["x"][i]=="Total" and d2["y"][i]=="Total"):
        l2.append([d2["area"][i], d2["sec"][i],d2["thr"][i]])
        
df1=pd.DataFrame(l1)
df2=pd.DataFrame(l2)

l3=[]
for i in range(len(df1)):
    one= df1[1][i]-df2[1][i]
    two= df2[1][i]-df2[2][i]
    thr= df2[2][i]
    p1= (one/df1[1][i])*100
    p2= (two/df1[1][i])*100
    p3= (thr/df1[1][i])*100
    
    l3.append([df1[0][i],p1,p2,p3])
    
df3=pd.DataFrame(l3)
df3.columns=["state-code","percent-one","percent-two","percent-three"]
df3.to_csv("percent-india.csv",index=False)
