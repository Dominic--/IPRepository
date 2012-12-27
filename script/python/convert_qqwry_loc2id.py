#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#  python convert_qqwry_loc2id.py address_file qqwry_file qqwry_file_left

import sys

f = open(sys.argv[1])
content = f.read()
f.close()

#建立id和loc的双重映射关系
content = content.split('\n')
id2loc = {}
loc2id = {}
for c in content:
	if len(c) > 5:
		c = c.split('\t')
		id2loc[c[0]] = c[1]
		loc2id[c[1]] = c[0]

f = open(sys.argv[2])
content = f.read()
f.close()
content = content.split('\n')

#寻找映射,完成转换
f = open(sys.argv[2], 'w')
for c in content:
	if len(c) > 5:
		c = c.split('\t')
		if c[2] in loc2id:
			c[2] = loc2id[c[2]]
			print '%s\t%s\t%s' % (c[0], c[1], c[2])
		else:
			f.write('%s\t%s\t%s\n' % (c[0], c[1], c[2]))

f.close()
