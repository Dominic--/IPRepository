#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python expand_ip.py cn.ip cn.ip.expand

import sys
import ipUtil

#cn
f = open(sys.argv[1])
content = f.read()
f.close()
content = content.split('\n')

f = open(sys.argv[2], 'w')
for c in content:
	if c.find('/') != -1:
		c = c.split('/')
		ip = c[0]
		cnt = int(2**(24-int(c[1])))
		for i in range(0, cnt):
			f.write('%s\n' % ip)
			ip = ipUtil.ipadd256(ip)
f.close()
