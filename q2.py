import numpy as np
import pandas as pd
import scipy.stats

cen=pd.read_excel("dataset/census.xlsx")
d1=pd.read_excel("dataset/DDW-C19-0000.xlsx")

cen2=cen[["Level","State","TRU","TOT_M","TOT_F"]]

l1=[]
l2=[]

l1.append([cen2["State"][0],cen2["TOT_M"][0]])
l2.append([cen2["State"][0],cen2["TOT_F"][0]])
for i in range(3,len(cen2)):
    if(cen2["Level"][i]=="STATE" and cen2["TRU"][i]=="Total"):
        l1.append([cen2["State"][i],cen2["TOT_M"][i]])
        l2.append([cen2["State"][i],cen2["TOT_F"][i]])

dfm1=pd.DataFrame(l1)
dff1=pd.DataFrame(l2)

dmale=d1[5:][d1[5:].columns[[0,3,4,6,9]]].reset_index(drop=True)
dmale.columns=["area","x","y","sec","thr"]
dfemale=d1[5:][d1[5:].columns[[0,3,4,7,10]]].reset_index(drop=True)
dfemale.columns=["area","x","y","sec","thr"]

lm=[]
for i in range(len(dmale)):
    if(dmale["x"][i]=="Total" and dmale["y"][i]=="Total"):
        lm.append([dmale["area"][i], dmale["sec"][i],dmale["thr"][i]])

lf=[]
for i in range(len(dfemale)):
    if(dfemale["x"][i]=="Total" and dfemale["y"][i]=="Total"):
        lf.append([dfemale["area"][i], dfemale["sec"][i],dfemale["thr"][i]])
        
dfm2=pd.DataFrame(lm)
dff2=pd.DataFrame(lf)

dfm2.columns=["area","two","three"]
dfm2["one"]=(dfm1[1]-dfm2["two"])/dfm1[1]*100
dfm2["two"]=(dfm2["two"]-dfm2["three"])/dfm1[1]*100
dfm2["three"]=dfm2["three"]/dfm1[1]*100

dff2.columns=["area","two","three"]
dff2["one"]=(dff1[1]-dff2["two"])/dff1[1]*100
dff2["two"]=(dff2["two"]-dff2["three"])/dff1[1]*100
dff2["three"]=dff2["three"]/dff1[1]*100


out1=dfm2[["area","one"]]
out1["female"]=dff2["one"]

out2=dfm2[["area","two"]]
out2["female"]=dff2["two"]

out3=dfm2[["area","three"]]
out3["female"]=dff2["three"]

out1["diff"]=abs(out1["one"]-out1["female"])
mean1=np.mean(out1["diff"])
zscore1=(out1["diff"]-mean1)/np.std(out1["diff"])
p_val1 = np.round(scipy.stats.norm.sf(abs(zscore1))*2,3)
out1["pval"]=p_val1
out1=out1.drop(columns="diff")
out1.columns=["state-code","male-percentage","female-percentage","p-value"]

out2["diff"]=abs(out2["two"]-out2["female"])
mean2=np.mean(out2["diff"])
zscore2=(out2["diff"]-mean2)/np.std(out2["diff"])
p_val2 = np.round(scipy.stats.norm.sf(abs(zscore2))*2,3)
out2["pval"]=p_val2
out2=out2.drop(columns="diff")
out2.columns=["state-code","male-percentage","female-percentage","p-value"]

out3["diff"]=abs(out3["three"]-out3["female"])
mean3=np.mean(out3["diff"])
zscore3=(out3["diff"]-mean3)/np.std(out3["diff"])
p_val3 = np.round(scipy.stats.norm.sf(abs(zscore3))*2,3)
out3["pval"]=p_val3
out3=out3.drop(columns="diff")
out3.columns=["state-code","male-percentage","female-percentage","p-value"]

out1.to_csv("gender-india-a.csv",index=False)
out2.to_csv("gender-india-b.csv",index=False)
out3.to_csv("gender-india-c.csv",index=False)
