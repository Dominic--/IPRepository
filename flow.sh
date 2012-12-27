#/bin/bash

case $1 in
#创建新的IPRepository,之前先完成备份
"create_new_ipr")
	if [ -f "./tmp/ipr" ]; then
		mv ./tmp/ipr ./back/ipr-back
	fi
	rm -f ./tmp/*
	sh ./script/create_location.sh
	sh ./script/parse_qqwry.sh
	sh ./script/merge_ipb_qqwry.sh
	sh ./script/create_ip_as.sh
	sh ./script/create_ip_isp.sh
	sh ./script/merge_ipb_isp.sh ;;

#建立世界(精确到国家)和中国(精确到县)的Loc和编码的对应关系表
#以下简称<地址编码表>
"create_location")
	sh ./script/create_location.sh ;;

#解析qqwry.dat二进制数据,并完成Loc和编码的映射
#生成IP(整数型)和Loc编码的对应关系
"parse_qqwry")
	sh ./script/parse_qqwry.sh ;;

#融合现有IPB数据和qqwry解析出来的数据
"merge_ipb_qqwry")
	sh ./script/merge_ipb_qqwry.sh ;;

#添加地址和编码的对应关系,建立全新的<地址编码表>
#此操作等同于完成create_location操作
"add_location")
	sh ./script/add_location.sh ;;

#建立IP和AS的对应关系,并完成一些统计
"create_ip_as")
	sh ./script/create_ip_as.sh ;;

#建立IP和ISP的对应关系
"create_ip_isp")
	sh ./script/create_ip_isp.sh ;;

#检测ISP数据的合理性
"check_isp")
	sh ./script/check_isp.sh ;;

#融合<IP,ISP>与IPB数据
"merge_ipb_isp")
	sh ./script/merge_ipb_isp.sh ;;

#通过调用淘宝API来修补冲突的IP项
#因为淘宝API的查询速度限制10qps,需要等待一段时间
"auto_modify_isp")
	sh ./script/auto_modify_isp.sh ;;

#清空所有临时文件(tmp目录下的所有文件)
"clear")
	rm -rf ./tmp/*
	cp ./back/qqwry.list ./tmp/qqwry.list ;;

#help选项
"help")
	echo "--------------------完整流程--------------------"
	echo "	create_new_ipr		创建新的IPRepository"
	echo "--------------------子模块流程------------------"
	echo "	create_location		1.创建地址和编码的<地址编码表>"
	echo "	parse_qqwry:		2.解析qqwry,生成IP和Loc编码对应(*需先完成第一步*)"
	echo "	merge_ipb_qqwry:	3.融合IPB和QQwry(*需先完成第二步*)"
	echo "	add_location:		手动添加地址信息(等同于完成第一步)"
	echo "	create_ip_as:		4.建立IP和AS的对应关系"
	echo "	create_ip_isp:		5.建立<IP,ISP>关系(*需先完成第4步*)"
	echo "	check_isp:		检查和旧有的ISP信息的对比度"
	echo "	auto_modify_isp:	通过淘宝IP&ISP纠正冲突项(*需先完成第4步*)"
	echo "	merge_ipb_isp:		6.融合ISP信息和Loc信息(*需先完成第五步*)"
	echo "	clear:			清空所有临时文件" ;;

*)
	echo "输入格式有误 >.<"
	echo "请输入以下命令,查看帮助信息:"
	echo "		./flow.sh help " ;;
esac
