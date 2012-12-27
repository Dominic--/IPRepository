#!/bin/bash

#把需要添加的地址(和地址编码)手动写入./data/location.list.add里
#手动执行此脚本后将会建立全新的地址信息库,所以需要顺序执行以下操作:
#	parse_qqwry
#	merge_ipb_qqwry
#以更新IP库的Loc信息。


echo "添加地址信息,写入location.list..."

#添加新对应关系至总表末尾
cat ./data/location.list.add >> ./tmp/location.list

#对总表排序按Loc编码排序
sort -o ./tmp/location.list ./tmp/location.list

#TODO
#可以在此脚本内完成最后的IP库更新,不要重新执行建库的操作
