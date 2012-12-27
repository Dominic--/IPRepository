#-*-coding:utf-8-*-

#Origin:
#  110000  北京市
#  110100    直辖市
#Goal:
#  110000  北京市
#  110100  北京市直辖市

#Usage:
#  python convert_location_txt2list.py filename

import sys

f = open(sys.argv[1])
content = f.read()
f.close()
content = content.split('\n')


#可知(短编码,短地址)的对应关系中,地址最大深度为3:
#	即省>市>县
#因此可根据适当的缩进来把短地址连接成长地址.
#转换过程中注意一些无用信息的过滤:(如市辖区等)

#当前县名
first = ""
#当前市名
second = ""
#当前省名
third = ""

#注意更新上一级Loc的时候,需要清空低级Loc信息
#如省名变化时,之前保存的市和县都需要清空
for c in content:
	#当有新的县名时
	if c.find("      ") > 0:
		#过滤无用信息
		if cmp(second, '市辖区') == 0 or cmp(second, '县') == 0 or cmp(second, '省直辖县级行政区划') or cmp(second, '自治区直辖县级行政区划'):
			second = ""
		third = c.split("      ")[1]
		id = c.split("      ")[0]
	
	#当有新的市名时
	elif c.find("    ") > 0:
		second = c.split("    ")[1]
		third = ""
		id = c.split("    ")[0]
	
	#当有新的省名时
	elif c.find("  ") > 0:
		first = c.split("  ")[1]
		second = ""
		third = ""
		id = c.split("  ")[0]

	#对短编码进行扩充,对短地址进行合并,完成转换
	print '%s\t%s%s%s' % ("1156"+id, first, second, third)
