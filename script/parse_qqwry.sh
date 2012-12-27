#!/bin/bash

#解析二进制qqwry.dat文件,生成IP段和Loc的对应关系
#转换点十分的IP段为整数型,
#根据之前生成的<地址编码表>把Loc转换成相应的Loc编码
#若不能完成Loc和Loc编码的转换,剩余条目留在原文件

echo "转换二进制qqwry.dat为文本形式,写入qqwry.list..."
#./bin/convert_qqwry_bin2text ./data/qqwry.dat > ./tmp/qqwry.list
cp ./back/qqwry.list ./tmp/qqwry.list

echo "qqwry.list中的IP从点十分转换为整数型,写入qqwry.num.list..."
python ./script/python/convert_qqwry_ip2num.py ./tmp/qqwry.list > ./tmp/qqwry.num.list

echo "转换qqwry.num.list中的Loc信息为标准地址编码,写入qqwry.num.id.list..."
echo "    qqwry.num.list中未找到对应关系的条目,保留在qqwry.num.list..."
python ./script/python/convert_qqwry_loc2id.py ./tmp/location ./tmp/qqwry.num.list > ./tmp/qqwry.num.id.list
