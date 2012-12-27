#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python merge_ip.py ipb.ip.expand cn.ip.expand

import sys

f = open(sys.argv[1])
ipb = f.read()
f.close()
ipb = ipb.split('\n')
ipb = set(ipb)

print "create ipb set"

f = open(sys.argv[2])
cn = f.read()
f.close()
cn = cn.split('\n')
cn = set(cn)

print "create cn set"

ip = cn | ipb
print "create merge set"

ip.sort()
print "sort"

for i in ip:
	print i
