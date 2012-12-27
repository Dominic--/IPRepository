#!/bin/bash

echo "建立as和isp的对应关系,写入as.isp..."
python ./script/python/create_as_isp.py ./data/backbone ./tmp/cn.as.sum ./data/asconn.txt ./tmp/as.isp

echo "通过as.isp和ip.as.cn生成ip.isp..."
python ./script/python/create_ip_isp.py ./tmp/as.isp ./tmp/ip.as.cn ./tmp/ip.isp
sort -n -o ./tmp/ip.isp ./tmp/ip.isp
