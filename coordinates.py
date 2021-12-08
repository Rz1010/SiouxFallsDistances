from geopy.distance import geodesic
import pandas as pd
with open('/home/fireflood/Desktop/SiouxFalls_node1.csv' ) as csv_file:
    columns1=["Node","X","Y"]
    df1 = pd.read_csv(csv_file,usecols=columns1)
    X=df1.X.tolist()
    Y=df1.Y.tolist()
with open('/home/fireflood/Desktop/SiouxFalls_net.csv' ) as csv_file:
    columns2 = ["LINK","A", "B"]
    df2 = pd.read_csv(csv_file, usecols=columns2)
    A=df2.A.tolist()
    B=df2.B.tolist()
milesA=[]
for i in range(76) :
    k1=(Y[A[i]-1],X[A[i]-1])
    k2=(Y[B[i]-1],X[B[i]-1])
    miles=geodesic(k2,k1).miles
    milesA.append(miles)
milesA=set(milesA)
    #milesA will have the distances