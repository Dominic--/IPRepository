#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python parse_aggr.py aggr.html

import sys, re

#清楚html标签
def stripTags(s):
	intag = [False]
	def chk(c):
		if intag[0]:
			intag[0] = (c != '>')
			return False
		elif c == '<':
			intag[0] = True
			return False
		return True
	return ''.join(c for c in s if (chk(c)))


f = open(sys.argv[1])
content = f.read()
f.close()

pre_re = re.compile('<PRE>(.*?)</PRE>', re.M|re.S)
pre = pre_re.findall(content)

f = file(sys.argv[2], 'w')
for p in pre:
	asNum = re.findall(r'<A NAME=\"(.*)\">', p)
	prefix_re = re.compile(r'^.*\n.*\n.*\n')
	p = prefix_re.sub("", p)
	red_re = re.compile(r'<font color=\"red\">.*</font>\n')
	p = red_re.sub("", p)
	p = stripTags(p)
	del_re = re.compile(r'\+.*\n')
	p = del_re.sub("\n", p)
	p = p.split("\n")
	for pp in p:
		if pp.strip() == "":
			continue
		f.write('%s\t' % asNum[0])
		pp = pp.split(" ")
		f.write('%s\t' % pp[0].strip())
		for i in range(1, len(pp)):
			if pp[i].strip() != "":
				f.write('%s ' % pp[i].strip())
		f.write('\n')
f.close()
