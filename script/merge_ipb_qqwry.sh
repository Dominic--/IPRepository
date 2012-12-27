#!/bin/bash

#删除IPB中的无用信息,完成和QQwry数据的融合
#具体融合算法参见相关的python文件

echo "剔除ipb_origin.txt中无用信息,写入ipb.list..."
python ./script/python/clear_ipb.py ./data/ipb_origin.txt > ./tmp/ipb.list

echo "融合现有ipb数据和qqwry解析出来的数据,写入ipb.list.new..."
python ./script/python/merge_ipb_qqwry.py ./tmp/ipb.list ./tmp/qqwry.num.id.list > ./tmp/ipb.list.new
