#-*-coding:utf-8-*-

#Origin:
#
#Goal:
#

#Usage:
#	python merge_ipb_qqwry.py ipb.list qqwry.num.id.list

import sys

#读取两个输入文件,初始有序
f = open(sys.argv[1])
ipb = f.read()
f.close()

f = open(sys.argv[2])
qqwry = f.read()
f.close()

ipb = ipb.split('\n')
qqwry = qqwry.split('\n')
k = 0
j = 0

#同时顺序处理两个文件,直到一个处理完为止
while k < len(ipb)-1 and j < len(qqwry)-1:
	#取出每个条目进行处理
	i = ipb[k]
	q = qqwry[j]
	i = i.split('\t')
	q = q.split('\t')
	#处理主要原则:
	#	以IPB数据为主,
	#	当IPB没有对应IP段时,添加qqwry数据
	#	当IPB和qqwry数据段有重叠时,qqwry数据充当第二结果
	
	#主要考虑四个参数,IPB中的IP起始和终止数:i[0],i[1]
	#				  QQwry中IP起始和终止数:q[0],q[1]

	#当QQwry某条目的起始数比IPB的终止数大
	#说明两者没有重叠,输出IPB条目,对比指针往后移动
	if int(q[0]) > int(i[1]):
		print '%s\t%s\t%s\t%s\t%s' % (i[0], i[1], i[2], i[3], i[4])
		k += 1
		continue

	#当IPB某条目的起始数比QQwry的终止数大
	#同样说明没有重叠,输出QQwry条目,对比指针往后移动
	elif int(q[1]) < int(i[0]):
		print '%s\t%s\t%s\t%d\t%d' % (q[0], q[1], q[2], 0, 0)
		j += 1
		continue

	#当QQwry的起始数位于IPB的地址段内
	#A.此时:i[0] <= q[0] <= i[1]
	elif int(q[0]) >= int(i[0]):
		#如果QQwry和IPB的起始数不同,它们之间的地址段可输出
		#然后调整起始数一致
		if int(q[0]) > int(i[0]):
			print '%s\t%d\t%s\t%s\t%s' % (i[0], int(q[0])-1, i[2], i[3], i[4])
			ipb[k] = '%s\t%s\t%s\t%s\t%s' % (q[0], i[1], i[2], i[3], i[4])
			continue

		#在起始数一致的情况下

		#1.IPB段比QQwry段要长,则输出重叠段,并调整IPB起始数为QQwry终止数加一
		elif int(i[1]) > int(q[1]):
			print '%s\t%s\t%s\t%s\t%s' % (i[0], q[1], i[2], q[2], i[4])
			ipb[k] = '%d\t%s\t%s\t%s\t%s' % (int(q[1])+1, i[1], i[2], i[3], i[4])
			j += 1
			continue
		#2.若两个IP段完全重叠,则直接输出,移动指针
		elif int(i[1]) == int(q[1]):
			print '%s\t%s\t%s\t%s\t%s' % (i[0], i[1], i[2], q[2], i[4])
			k += 1
			j += 1
			continue
		#3.与第1种情况类似
		elif int(i[1]) < int(q[1]):
			print '%s\t%s\t%s\t%s\t%s' % (i[0], i[1], i[2], q[2], i[4])
			qqwry[j] = '%d\t%s\t%s' % (int(i[1])+1, q[1], q[2])
			k += 1
			continue
	#B.与A情况类似.调整QQwry的起始位置后,变成A情况.
	elif int(q[0]) < int(i[0]):
			print '%s\t%s\t%s\t%d\t%d' % (q[0], q[1], q[2], 0, 0)
			qqwry[j] = '%d\t%s\t%s' % (int(i[1])+1, q[1], q[2])
			continue

#把上一步中没有遍历完的文件剩余部分直接输出
while k < len(ipb)-1:
	print ipb[k]
	k += 1
while j < len(qqwry)-1:
	print qqwry[j]
	j += 1
