#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python select_ip_as_cn.py ip.as cn.ip.expand ip.as.expand cn.as.sum ip.as.cn

from __future__ import division
import sys, ipUtil

#通过cn.ip.expand建立中国IP的字典
f = open(sys.argv[2])
content = f.read()
f.close()
content = content.strip().split('\n')

cn = {}
for c in content:
	cn[c] = 1

#读入ip.as,即IP(未expand)和AS的对应关系
f = open(sys.argv[1])
content = f.read()
f.close()
content = content.strip().split('\n')

#扩展IP
f = file(sys.argv[3], 'w')
#统计AS中China部分
fcn = file(sys.argv[4], 'w')
#统计中国IP(已expand)对应的中国AS
fcnip = file(sys.argv[5], 'w')

#具体算法实现
#一边扩展ip.as同时进行是否属于中国IP的判断

lastAS = ""
lastCN = 0
printLine = ""
sum = 0
csum = 0
asNum = ""
ass = ""
for c in content:
	c = c.split('\t')
	if cmp(c[0], lastAS) != 0:
		asNum = c[0]
		ass = c[2]
		csum = 0
		sum = 0
		if lastCN > 0:
			fcn.write(printLine)
	ips = c[1].split('/')
	ip = ips[0]
	for i in range(0, int(2**(24-int(ips[1])))):
		if cn.has_key(ip):
			f.write('%s\t%s\t%d\t%s\n' % (asNum, ip, 1, ass))
			fcnip.write('%s\t%s\n' % (ip, asNum))
			csum = csum + 1
		else:
			f.write('%s\t%s\t%d\t%s\n' % (asNum, ip, 0, ass))
		ip = ipUtil.ipadd256(ip)
		sum = sum + 1
	if csum > 0:
		printLine = '%s\t%d\t%d\t%f\n' % (asNum, sum, csum, csum/sum*100)
	lastAS = asNum
	lastCN = csum
f.close()
fcn.close()
fcnip.close()
