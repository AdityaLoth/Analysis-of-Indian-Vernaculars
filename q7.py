import numpy as np
import pandas as pd

AP= pd.read_excel("dataset/ANDHRA PRADESH.XLSX")
AP=AP[5:]
ARP= pd.read_excel("dataset/ARUNACHAL PRADESH.XLSX")
ARP=ARP[5:]
AAN= pd.read_excel("dataset/ANDAMAN AND NICOBAR.XLSX")
AAN=AAN[5:]
AS= pd.read_excel("dataset/ASSAM.XLSX")
AS=AS[5:]
B= pd.read_excel("dataset/BIHAR.XLSX")
B=B[5:]
CH= pd.read_excel("dataset/CHANDIGARH.XLSX")
CH=CH[5:]
CG= pd.read_excel("dataset/CHHATISGARH.XLSX")
CG=CG[5:]
DNH= pd.read_excel("dataset/DADRA AND NAGAR HAVELI.XLSX")
DNH=DNH[5:]
DD= pd.read_excel("dataset/DAMAN AND DIU.XLSX")
DD=DD[5:]
D= pd.read_excel("dataset/DELHI.XLSX")
D=D[5:]
G= pd.read_excel("dataset/GOA.XLSX")
G=G[5:]
GJ= pd.read_excel("dataset/GUJARAT.XLSX")
GJ=GJ[5:]
HR= pd.read_excel("dataset/HARYANA.XLSX")
HR=HR[5:]
HP= pd.read_excel("dataset/HIMACHAL PRADESH.XLSX")
HP=HP[5:]
JK= pd.read_excel("dataset/JAMMU AND KASHMIR.XLSX")
JK=JK[5:]
JH= pd.read_excel("dataset/JHARKHAND.XLSX")
JH=JH[5:]
KT= pd.read_excel("dataset/KARNATAKA.XLSX")
KT=KT[5:]
KR= pd.read_excel("dataset/KERALA.XLSX")
KR=KR[5:]
L= pd.read_excel("dataset/LAKSHDWEEP.XLSX")
L=L[5:]
MP= pd.read_excel("dataset/MADHYA PRADESH.XLSX")
MP=MP[5:]
MH= pd.read_excel("dataset/MAHARASHTRA.XLSX")
MH=MH[5:]
MN= pd.read_excel("dataset/MANIPUR.XLSX")
MN=MN[5:]
MG= pd.read_excel("dataset/MEGHALAYA.XLSX")
MG=MG[5:]
MZ= pd.read_excel("dataset/MIZORAM.XLSX")
MZ=MZ[5:]
NG= pd.read_excel("dataset/NAGALAND.XLSX")
NG=NG[5:]
OR= pd.read_excel("dataset/ODISHA.XLSX")
OR=OR[5:]
PD= pd.read_excel("dataset/PUDUCHERRY.XLSX")
PD=PD[5:]
PN= pd.read_excel("dataset/PUNJAB.XLSX")
PN=PN[5:]
RJ= pd.read_excel("dataset/RAJASTHAN.XLSX")
RJ=RJ[5:]
SK= pd.read_excel("dataset/SIKKIM.XLSX")
SK=SK[5:]
TN= pd.read_excel("dataset/TAMIL NADU.XLSX")
TN=TN[5:]
TP= pd.read_excel("dataset/TRIPURA.XLSX")
TP=TP[5:]
UP= pd.read_excel("dataset/UTTAR PRADESH.XLSX")
UP=UP[5:]
UT= pd.read_excel("dataset/UTTRAKHAND.XLSX")
UT=UT[5:]
WB= pd.read_excel("dataset/WEST BENGAL.XLSX")
WB=WB[5:]

north=[JK,L,PN,HP,HR,UT,D,CH]
west=[RJ,GJ,MH,G,DNH,DD]
central=[MP,UP,CG]
east=[B,WB,OR,JH]
south=[KT,AP,TN,KR,L,PD]
northeast=[AS,SK,MG,TP,ARP,MN,NG,MZ,AAN]

regionlist=[north,west,central,east,south,northeast]

out1=[]
out2=[]
for region in regionlist:
    one=pd.DataFrame([])    
    common=pd.DataFrame([])
    for state in region:
        first=state[state.columns[[3,4]]].dropna()
        first.columns=["x","y"]
        first=first.dropna().reset_index(drop=True)
        one=pd.concat([one,first])

        sec=state[state.columns[[8,9]]].dropna()
        sec.columns=["x","y"]
        sec=sec.groupby(["x"]).y.sum().to_frame("y").dropna().reset_index()

        third=state[state.columns[[13,14]]].dropna()
        third.columns=["x","y"]
        third=third.groupby(["x"]).y.sum().to_frame("y").dropna().reset_index()
        
        common=pd.concat([common,first,sec,third])
        
    mt=one.groupby(["x"]).y.sum().to_frame("y").dropna().reset_index()
    mt=mt.sort_values("y").reset_index(drop="True")
    lg1=mt.loc[len(mt)-1][0]
    lg2=mt.loc[len(mt)-2][0]
    lg3=mt.loc[len(mt)-3][0]

    com=common.groupby(["x"]).y.sum().to_frame("y").dropna().reset_index()
    com=com.sort_values("y").reset_index(drop="True")
    llg1=com.loc[len(com)-1][0]
    llg2=com.loc[len(com)-2][0]
    llg3=com.loc[len(com)-3][0]    
    
    out1.append(["r",lg1,lg2,lg3])
    out2.append(["r",llg1,llg2,llg3])     
    
regions=["North","West","Central","East","South","Northeast"]

part1=pd.DataFrame(out1)
part2=pd.DataFrame(out2)
part1.columns=["region","language-1","language-2","language-3"]
part2.columns=["region","language-1","language-2","language-3"]

for i in range(len(regions)):
    part1["region"][i]=regions[i]
    part2["region"][i]=regions[i]

part1=part1.sort_values("region").reset_index(drop=True)
part2=part2.sort_values("region").reset_index(drop=True)

part1.to_csv("region-india-a.csv",index=False)
part2.to_csv("region-india-b.csv",index=False)
