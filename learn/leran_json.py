#-*-coding:utf-8 -*-
import json
filename='username.json'
with open(filename)as dk:
    kd_date=json.load(dk)
    print(kd_date)
