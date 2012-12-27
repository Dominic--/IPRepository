#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python auto_modify_isp.py ip.isp conflict.isp

import urllib, sys, simplejson

f = open(sys.argv[2])
content = f.read()
f.close()
content = content.split("\n")

f = file("./test.txt", "wa")
baseUrl = "http://ip.taobao.com/service/getIpInfo.php?ip="
for c in content:
	if c.strip() == "":
		continue
	j = simplejson.loads(urllib.urlopen(baseUrl+c).read())
	if j["code"] == 0:
		#print ('%s\t%s\n' % (c, j["data"]["isp"].encode("utf-8")))
		f.write('%s\t%s\n' % (c, j["data"]["isp"].encode("utf-8")))
f.close()

