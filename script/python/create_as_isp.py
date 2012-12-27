#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python create_ip_isp.py backbone cn.as.sum asconn.txt as.isp

import sys

asType = ""

def recurse(asconn, csum, bb, adj, cnt):
	global asType
	if cnt == 3:
		return
	adj = adj.split(" ")
	for a in adj:
		if csum.has_key("AS"+a):
			if csum["AS"+a] < 1:
				continue
		else:
			continue
		if bb.has_key("AS"+a):
			asType = asType + " " + bb["AS"+a]
			asType = trim_as(asType.strip())
		else:
			cnt = cnt + 1
			if asconn.has_key("AS"+a):
				recurse(asconn, csum, bb, asconn["AS"+a], cnt)
			cnt = cnt - 1

def trim_as(ass):
	ass = ass.split(" ")
	ass = set(ass)
	return " ".join(list(ass))

#Init bb(backbone)
f = open(sys.argv[1])
content = f.read()
f.close()
content = content.split("\n")

bb = {}
for c in content:
	if c.strip() == "":
		continue
	c = c.split("\t")
	bb["AS"+c[0]] = c[1]

#Init csum
f = open(sys.argv[2])
content = f.read()
f.close()
content = content.split("\n")

csum = {}
for c in content:
	if c.strip() == "":
		continue
	c = c.split("\t")
	csum[c[0]] = c[3]

#Init asconn
f = open(sys.argv[3])
content = f.read()
f.close()
content = content.split('\n')

asconn = {}
for c in content:
	if c.strip() == "":
		continue
	c = c.split(":")
	asNum = c[0].strip()
	up = c[1].strip()
	down = c[2].strip()
	asconn["AS"+asNum] = up + " " + down

#create as-isp
f = file(sys.argv[4], 'w')
for a,c in csum.items():
	if c < 1:
		f.write('%s\tETC\n' % a)
	if bb.has_key(a):
		f.write('%s\t%sBB\n' % (a,bb[a]))
	else:
		asType = ""
		if asconn.has_key(a):
			recurse(asconn, csum, bb, asconn[a], 1)
		if asType == "":
			asType = "ETC"
		f.write('%s\t%s\n' % (a, asType))
