# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:51:41 2019

@author: 毛征明
"""
import pandas as pd
import re
f=open("服创大赛-原始数据.csv")
import time, datetime
raw_data=pd.read_csv(f,usecols=[0,1,2,3])
#1 clean
def iter_sub(df):
    try:
        return re.sub("\D","",df["imsi"])
    except:
        pass
raw_data['imsi']=raw_data.apply(iter_sub,axis=1)
raw_data=raw_data.dropna()

def iter_time_tran(df):
    times=df['timestamp']//1000
    timeArray = time.localtime(times)
    return time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
raw_data['timestamp']=raw_data.apply(iter_time_tran,axis=1)

def iter_time_filter(df):
    if not re.match('2018--10--03',df['timestamp']):
        return "nope"
    else:
        return df['timestamp']
raw_data['timestamp']=raw_data.apply(iter_time_filter,axis=1)
raw_data=raw_data[raw_data['timestamp']!="nope"]

file=open("服创大赛-基站经纬度数据.csv")
lac_data=pd.read_csv(file)
lac_data=lac_data.drop('laci',axis=1).join(lac_data['laci'].str.split('-',expand=True))
lac_data.rename(columns={0:"lac_id",1:"cell_id"},inplace=True)

