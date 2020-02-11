# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:04:48 2020

@author: 毛征明
"""

import requests
import json

parameters=dict()

base_url="https://restapi.amap.com/v3/place/polygon?key=3c60df6b7aa67ecdce97874711c2f085"
parameters["polygon"]="122.3508,41.08806;124.0002823,42.50168"
parameters["offset"]="25"
parameters["page"]="1"

req=1
while(req!=30000):
    