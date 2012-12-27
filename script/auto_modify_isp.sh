#!/bin/bash

echo "通过淘宝IP库更新现有的冲突项,合并到ip.isp..."
python ./script/python/auto_modify_isp.py ./tmp/ip.isp ./tmp/conflict.ip
