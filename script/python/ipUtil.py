import struct, socket
def dottedQuadToNum(ip):
	"convert decimal dotted quad string to long integer"
	return socket.ntohl(struct.unpack('I',socket.inet_aton(ip))[0])

def numToDottedQuad(n):
	"convert long int to dotted quad string"
	return socket.inet_ntoa(struct.pack('I',socket.htonl(n)))

def maskToNum(mask):
	"convert  CIDR mask to binary mask"
	return (2**32 -1) ^ (2**(32 - int(mask)) - 1)

def maskIPToMask(maskip):
	"convert 255.255.255.0 to 24"
	ipnum = dottedQuadToNum(maskip)
	ret = 0
	while ipnum > 0:
		if ipnum & 0x1 == 1:
			ret += 1
		ipnum = ipnum >> 1
	return ret

def CIDRBcastIP(ipmask):
	"return CIDR broadcast IP"
	a,b = ipmask.split("/")
	ip = dottedQuadToNum(a)
	mask = maskToNum(b)
	return numToDottedQuad(ip | ((2**32 -1) & ~mask))
def CIDRNetIP(ipmask):
	"return CIDR network IP"
	a,b = ipmask.split("/")
	ip = dottedQuadToNum(a)
	mask = maskToNum(b)
	return numToDottedQuad(ip & mask)

def __reduceip(ipstart, ipend):
	#count leading 1 pos
	ret = []
	first = ipstart
	while first <= ipend:
		if first == ipend:
			ret += [(first, 2**32 -1)]
			break
		sizemask = 0
		len = ipend - first + 1
		while len != 1:
			sizemask +=1
			len = len >> 1
		firstmask = 0 
		tmp = first
		while (tmp & 0x1) == 0:
			firstmask += 1
			tmp = tmp >> 1
		if firstmask > sizemask:
			mask = (2 **32 - 1) & ( ~ (2** sizemask - 1))
		else:
			mask = (2 **32 - 1) & ( ~ (2** firstmask - 1))
		ret += [(first, mask)]
		first = (2**32 -1) & (first | ~mask) + 1
	return ret
		
	
def reduce(ipmasks):
	"""
	this module is used to reduce continous ip/mask to a big one.
	ex:
		166.111.8.0/24	\
		166.111.9.0/24	|=> 166.111.8.0/23 + 166.111.10.0/24	
		166.111.10.0.24 /
	intput : ipmasks, every entry is a tuple (ipnum, masknum) 
	ourput : same as input , is an array , every entry is a tuple (ipnum, masknum)
	"""
	ret = []
	first = last = 0
	for ip, mask in ipmasks:
		if int(ip) != ip or int(mask) != mask:
			raise "ip or mask is not a num"
		ipmin = ip & mask
		ipmax = ip | (~mask & 2**32 - 1)
		#pass first
		if first == 0:
			first = ipmin
			last = ipmax
			continue
		if last == ipmin - 1:
			last = ipmax
		else:
			ret += __reduceip(first, last)
			first = ipmin
			last = ipmax 
	#calculate last
	ret +=__reduceip(first, ipmax)
	return ret

def ipadd1(ip):
	ip = ip.split('.')
	ip1 = int(ip[0])
	ip2 = int(ip[1])
	ip3 = int(ip[2])
	ip4 = int(ip[3])+1

	if ip4 == 256:
		ip4 = 0
		ip3 = ip3 + 1
		if ip3 == 256:
			ip3 = 0
			ip2 = ip2 + 1
			if ip2 == 256:
				ip2 = 0
				ip1 = ip1 + 1
	return '%d.%d.%d.%d' % (ip1, ip2, ip3, ip4)

def ipadd256(ip):
	ip = ip.split('.')
	ip1 = int(ip[0])
	ip2 = int(ip[1])
	ip3 = int(ip[2]) + 1
	
	if ip3 == 256:
		ip3 = 0
		ip2 = ip2 + 1
		if ip2 == 256:
			ip2 = 0
			ip1 = ip1 + 1
	
	return '%d.%d.%d.0' % (ip1, ip2, ip3)


if __name__ == "__main__":
	print CIDRNetIP("167.139.0.0/16")
	print CIDRBcastIP("167.139.0.0/16")
	print CIDRBcastIP("10.12.131.1/25")
	pass
