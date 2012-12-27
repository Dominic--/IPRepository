#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python create_ip_isp.py as.isp ip.as.cn ip.isp

import sys, ipUtil

f = open(sys.argv[1])
content = f.read()
f.close()
content = content.split('\n')

as2ips = {}
for c in content:
	if c.strip() == "":
		continue
	c = c.split('\t')
	as2ips[c[0]] = c[1]

f = open(sys.argv[2])
content = f.read()
f.close()
content = content.split('\n')

f = file(sys.argv[3], 'w')
for c in content:
	if c.strip() == "":
		continue
	c = c.split('\t')
	if as2ips.has_key(c[1]):
		f.write('%s\t%s\t%s\n' % (ipUtil.dottedQuadToNum(c[0]), ipUtil.dottedQuadToNum(ipUtil.ipadd256(c[0]))-1, as2ips[c[1]]))
	else:
		f.write('%s\t%s\tETC\n' % (ipUtil.dottedQuadToNum(c[0]), ipUtil.dottedQuadToNum(ipUtil.ipadd256(c[0]))-1))
f.close()
