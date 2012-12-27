#!/bin/bash

echo "备份原有的bgp数据..."
#mv -f ./data/aggr.html ./data/asconn.txt ./data/asnames.txt ./back

echo "获取最新的aggr.html, asconn.txt, asnames.txt..."
#wget -O ./data/aggr.html http://www.cidr-report.org/as2.0/aggr.html
#wget -O ./data/asconn.txt http://bgp.potaroo.net/as2.0/asconn.txt
#wget -O ./data/asnames.txt http://bgp.potaroo.net/as2.0/asnames.txt

echo "自cnnic获得中国IP,写入cn.ip..."
python ./script/python/get_ip.py ./data/cnnic.html.src ./tmp/cn.ip

echo "扩展cn.ip中的ip,写入cn.ip.expand..."
python ./script/python/expand_ip.py ./tmp/cn.ip ./tmp/cn.ip.expand

echo "解析aggr.html,生成AS和IP的对应关系,写入ip.as..."
python ./script/python/parse_aggr.py ./data/aggr.html ./tmp/ip.as

echo "扩展ip.as,判断中国IP,写入ip.as.expand,中国部分写入cn.as.sum..."
python ./script/python/select_cn_ip_as.py ./tmp/ip.as ./tmp/cn.ip.expand ./tmp/ip.as.expand ./tmp/cn.as.sum ./tmp/ip.as.cn
