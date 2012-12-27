#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python check_isp.py ip.isp ip.type conflict.ip

from __future__ import division
import sys, ipUtil


def strin(a, b):
	a = a.strip().split(" ")
	b = b.strip()
	for aa in a:
		if b.find(aa) < 0:
			return False
	return True


f = open(sys.argv[1])
my = f.read()
f.close()
my = my.split("\n")

f = open(sys.argv[2])
your = f.read()
f.close()
your = your.split("\n")

y = {}
for c in your:
	if c.strip() == "":
		continue
	c = c.split("\t")
	y[c[0]] = c[1]

f = file(sys.argv[3], 'w')
miny = 0
meqy = 0
yinm = 0
sum = 0
yy = ""
for c in my:
	if c.strip() == "":
		continue
	c = c.split("\t")
	c0 = ipUtil.numToDottedQuad(long(c[0]))
	if y.has_key(c0):
		yy = y[c0]
		sum = sum + 1
		if yy == c[2]:
			meqy = meqy + 1
		elif strin(yy, c[2]):
			yinm = yinm + 1
		elif strin(c[2], yy):
			miny = miny + 1
		else:
			f.write('%s\n' % c0)
	else:
		f.write('%s\n' % c0)	
f.close()

print "sum-my:\n"
print '%d\n' % len(my)
print "sum-your:\n"
print '%d\n' % len(y)
print "sum-same-prefix:\n"
print '%d\n' % sum
print "meqy:\n"
print '%s\n' % str(meqy/sum)
print "yinm:\n"
print '%s\n' % str(yinm/sum)
print "miny:\n"
print '%s\n' % str(miny/sum)
