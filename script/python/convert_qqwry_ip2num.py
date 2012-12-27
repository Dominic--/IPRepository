#-*-coding:utf-8-*-

#Origin:
#	0.0.0.0 0.0.0.1 Loc1 Loc2
#Goal:
#	0 1 Loc1 Loc2

#Usage:
#	python convert_qqwry_ip2num.py filename

import sys
import ipUtil

f = open(sys.argv[1])
content = f.read()
f.close()

content = content.split('\n')
for c in content:
	if c.find('\t') != -1:
		c = c.split('\t')
		print '%d\t%d\t%s' % (ipUtil.dottedQuadToNum(c[0]), ipUtil.dottedQuadToNum(c[1]), c[2])
