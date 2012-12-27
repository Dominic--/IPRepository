#-*-coding:utf-8-*-

#Origin:
#  ip1,ip2,int1,int2,loc1-1,loc1-2,loc2-1,loc2-2,loc3-1,loc3-2
#Goal:
#  int1,int2,loc1-2,loc2-2,loc3-2

#Usage:
#  python clear_ipb.py ipb_file

import sys

f = open(sys.argv[1])
content = f.read()
f.close()

content = content.split('\n')
for c in content:
	if len(c) > 5:
		c = c.split(',')
		print '%s\t%s\t%s\t%s\t%s' % (c[2], c[3], c[5], c[7], c[9])
