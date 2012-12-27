#/bin/bash

echo "融合ipb.list.new和ip.isp,写入ipb.list.isp.new..."
python ./script/python/merge_ipb_isp.py ./tmp/ipb.list.new ./tmp/ip.isp > ./tmp/ipb.list.isp.new

echo "创建IPR完毕,最后文件写入ipr..."
cp ./tmp/ipb.list.isp.new ./tmp/ipr
cp ./tmp/ipr ./result/ipr
