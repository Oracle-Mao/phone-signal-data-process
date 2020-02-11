# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:49:51 2020

@author: 毛征明
"""

from math import sin, asin, cos, radians, fabs, sqrt
import random

def caculate_distance(lat0,lat1,lon0,lon1):
    lat0,lat1,lon0,lon1=map(radians,[lat0,lat1,lon0,lon1])
    dlon = fabs(lon0 - lon1)
    dlat = fabs(lat0 - lat1)
    h=sin(dlat/2)**2+cos(lat0)*cos(lat1)*sin(dlon/2)**2
    dis=2 *6371*asin(sqrt(h))#6371 is length of raidus
    return dis

def NN(coordinate,BL):
    ret=0
    nearest=6371*6.3
    for i in range(len(BL)):
        dis=caculate_distance(coordinate[1],BL[i][1],coordinate[0],BL[i][0])
        if dis<nearest:
            nearest=dis
            ret=i
    return ret

def MonteCarlo(N,BL):
    #range => "122.3508,41.08806;124.0002823,42.50168"
    ret=[0]*len(BL)
    for _ in range(N):
        lon=random.uniform(122.3508,124.0002823)
        lat=random.uniform(41.08806,42.50168)
        ret[NN([lat,lon],BL)]+=1
    return ret 