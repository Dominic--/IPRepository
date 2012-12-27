#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python get_ip.py cnnic.html.src cn.ip

import urllib, sys, re
import ipUtil
from BeautifulSoup import BeautifulSoup

#cnnicURL = "http://ipwhois.cnnic.cn/ipstats/detail.php?obj=ipv4&coun";
#htmlSrc = urllib.urlopen(cnnicURL).read()
f = open(sys.argv[1])
htmlSrc = f.read();
f.close()

f = file(sys.argv[2], 'w')
ip = re.findall(r'searchtext=(.*)\" ',htmlSrc)
for i in ip:
	f.write('%s\n' % i)
f.close()
