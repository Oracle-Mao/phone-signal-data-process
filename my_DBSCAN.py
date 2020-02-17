# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:48:23 2020

@author: 毛征明
"""

import json
import requests
f=open("D:\C_research\服务外包\交通时空大数据分析挖掘系统-数据\clean_data.json")
clean_data=json.load(f)

address=[]
for i in range(len(clean_data["cell_id"])):
    url="http://api.cellocation.com:81/cell/?mcc=460&mnc=1&lac={}&ci={}&output=json".format(clean_data["lac_id"][i],clean_data["cell_id"][i])
    ret=requests.get(url).content
    ret=json.loads(ret)
    address.append((ret["lat"],ret["lon"]))


from math import sin, asin, cos, radians, fabs, sqrt
import random

UNCLASSIFIED = False
NOISE = 0

def caculate_distance(p1,p2):
    lat0,lat1,lon0,lon1=map(radians,[p1[1],p2[1],p1[0],p2[0]])
    dlon = fabs(lon0 - lon1)
    dlat = fabs(lat0 - lat1)
    h=sin(dlat/2)**2+cos(lat0)*cos(lat1)*sin(dlon/2)**2
    dis=2 *6371*asin(sqrt(h))#6371 is length of raidus
    return dis



def extract_eps(pointID,li,eps=0.5):
    ret=[]
    point=li[pointID]
    for j in range(len(li)):
        if caculate_distance(point,li[j])<eps:
            ret.append(j) 
    return ret

def extend(data, clusterResult, pointId, clusterId,minPts):    
    eps=extract_eps(pointId,data)
    if len(eps)<minPts:
        clusterResult[pointId]=NOISE
        return False
    else:
        clusterResult[pointId] = clusterId
        for q in eps:
            clusterResult[q] = clusterId
        while len(eps) > 0:
            currentPoint = eps[0]
            ret=extract_eps(currentPoint,data)
            if len(ret)>=minPts:
                for i in range(len(ret)):
                    retPoint = ret[i]
                    if clusterResult[retPoint] == UNCLASSIFIED:
                        eps.append(retPoint)
                        clusterResult[retPoint] = clusterId
                    elif clusterResult[retPoint] == NOISE:
                        clusterResult[retPoint] = clusterId
            eps=eps[1:]
        return True
    

def DBSCAN(data):
    clusterId = 1
    nPoints = len(data)
    clusterResult = [UNCLASSIFIED] * nPoints
    minPts=nPoints//10
    for pointId in range(nPoints):
        if clusterResult[pointId] == UNCLASSIFIED:
            if extend(data, clusterResult, pointId, clusterId, minPts):
                clusterId = clusterId + 1
    return clusterResult
    

