import numpy as np
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt

cen=pd.read_excel("dataset/census.xlsx")
d1=pd.read_excel("dataset/DDW-C19-0000.xlsx")
cen2=cen[["Level","State","TRU","TOT_P"]]

cen2=cen2[cen2["Level"]=="STATE"]
cen2=cen2[cen2["TRU"]!="Total"]
cen2=cen2.reset_index(drop="True")

d2=d1[5:][d1[5:].columns[[0,3,4,5,8]]].reset_index(drop=True)
d2.columns=["area","x","y","sec","thr"]
d2=d2[d2["x"]!="Total"]
d2=d2[d2["y"]=="Total"].reset_index(drop="True")
d2=d2[2:].reset_index(drop="True")

d2["one"]=(cen2["TOT_P"]-d2["sec"])/cen2["TOT_P"]
d2["sec"]=(d2["sec"]-d2["thr"])/cen2["TOT_P"]
d2["thr"]=d2["thr"]/cen2["TOT_P"]
rural=d2[d2["x"]=="Rural"].reset_index(drop="True")
urban=d2[d2["x"]=="Urban"].reset_index(drop="True")

out1=urban[["area","one"]]
out1["u"]=rural["one"]
out1.columns=["state-code","urban-percentage","rural-percentage"]

out2=urban[["area","sec"]]
out2["u"]=rural["sec"]
out2.columns=["state-code","urban-percentage","rural-percentage"]

out3=urban[["area","thr"]]
out3["u"]=rural["thr"]
out3.columns=["state-code","urban-percentage","rural-percentage"]

out1["diff"]=abs(out1["urban-percentage"]-out1["rural-percentage"])
mean1=np.mean(out1["diff"])
zscore1=(out1["diff"]-mean1)/np.std(out1["diff"])
p_val1 = np.round(scipy.stats.norm.sf(abs(zscore1.astype(float)))*2,3)
out1["p-value"]=p_val1
out1=out1.drop(columns="diff")

out2["diff"]=abs(out2["urban-percentage"]-out2["rural-percentage"])
mean2=np.mean(out2["diff"])
zscore2=(out2["diff"]-mean2)/np.std(out2["diff"])
p_val2 = np.round(scipy.stats.norm.sf(abs(zscore2.astype(float)))*2,3)
out2["p-value"]=p_val2
out2=out2.drop(columns="diff")

out3["diff"]=abs(out3["urban-percentage"]-out3["rural-percentage"])
mean3=np.mean(out3["diff"])
zscore3=(out3["diff"]-mean3)/np.std(out3["diff"])
p_val3 = np.round(scipy.stats.norm.sf(abs(zscore3.astype(float)))*2,3)
out3["p-value"]=p_val3
out3=out3.drop(columns="diff")

out3.to_csv("geography-india-c.csv",index=False)
out2.to_csv("geography-india-b.csv",index=False)
out1.to_csv("geography-india-a.csv",index=False)

