# coding: utf-8
import os
import subprocess
import requests
import json
import sys


def getoutput(address):
    command = "dig @114.114.114.114 +trace "+address
    r = os.popen(command)
    info = r.readlines()
    list = []
    for line in info:
        line = line.strip("\r\n")
        if ("from" in line):
            x = line.find("from")
            y = line.find("#")
            subline = line[x + 5:y]
            list.append(subline)
    return list
# 遍历列表中的ip值 查询api获得其所在地理位置
def get_the_loc(arr):
    x = 0
    origin = {}
    dic_all_in_all = []
    # print len(arr)
    dic_destination=[]
    for ip in arr:
        r = requests.get("http://ip-api.com/json/"+ip)
        python_obj = json.loads(r.text)
        city = {"address": python_obj["city"]}
        latitude = python_obj["lat"]
        longitude = python_obj["lon"]
        if x == 0:
            origin["latitude"] = latitude
            origin["longitude"] = longitude
            x += 1
        else:
            dic = {}
            dic["latitude"] = latitude
            dic["longitude"] = longitude
            dic_a={}
            dic_a["origin"]=origin
            dic_a["destination"]=dic
            dic_all_in_all.append(dic_a)
            dic_destination.append(dic)
    return dic_all_in_all
add = sys.argv[1];
result = get_the_loc(getoutput(add));
result = json.dumps(result, ensure_ascii=False)
print result

