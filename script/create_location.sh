#!/bin/bash

#通过解析已有数据(./data/location.txt)建立中国(精确到县)Loc和编码的对应关系表,
#以下简称<地址编码表>
#并完成中国和世界(精确到国家)Loc的融合,保证最后按地址编码升序


echo "转换location.txt中的节点对应为详细地址对应,写入location.cn..."

#解析初始数据中的(短编码,短地址)对应为最终的(长编码,长地址)对应关系
python ./script/python/convert_location_txt2list.py ./data/location.txt > ./tmp/location.cn

echo "合并中国地址信息(location.cn)和世界地址信息(country.txt),写入location..."

#融合世界Loc编码和中国Loc编码
cat ./tmp/location.cn >> ./tmp/location.tmp
cat ./data/country.txt >> ./tmp/location.tmp

#对Loc编码进行升序排列
sort -o ./tmp/location ./tmp/location.tmp
cp ./tmp/location ./result/location
