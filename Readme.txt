--------------------Information---------------------------
Author: Dominic
Mobile: 86-15901511022
E-Mal:	linheng_mail@126.com
Hint:	Any Question or Bug is welcome to let me know

-----------------------Usage-------------------------------
Just Type:
	./flow.sh help
Best Wishes~

-----------------Description Of Files----------------------

README.md:  					Readme file for github server;
README.txt:						Readme file for IPRepository(you are reading it now! >.<);
where.is.me:					Record what I have done, and what should done (- -!);

flow.sh:						Main Shell (type "./flow.sh --help" for more informations)

back/:							Directory of backup files
  aggr.html						Html source file which download from web;
  qqwry.list					Textfile of qqwry.dat which parsed by flow.sh;

bin/:							Directory of executable file
  convert_qqwry_bin2text:		Parse qqwry.dat to readable format(Textfile)

data/:							Directory of origin data;
  aggr.html						Html source file which download from web;
  asconn.txt					File containing AS upstream/downstream ASes;
  asnames.txt					File containing AS's number and AS's Name
  backbone						Containing China backbone ASes
  cnnic.html.src 				File of China IPs;
  country.txt 					Location(World) informations file from ISO
  ipb_origin.txt:				IPB file from 17 companies
  location.txt 					Location(China) informations file from stats.gov.cn
  qqwry.dat:					IP location binary file from QQ

script/:						Directory of script files
  add_location.sh:				Add Loc&Code item to location.list
  auto_modify_isp.sh			Modify isp information by querying TaoBao API
  check_isp.sh					Check difference between Origin/Mine <IP, ISP>
  create_ip_as.sh				Create <IP, AS> mapping file
  create_ip_isp.sh				Create <IP, ISP> mapping file
  create_location.sh:			Create one new location.list
  merge_ipb_isp.sh				Merge ipb&isp data
  merge_ipb_qqwry.sh:			Merge qqwry and ipb
  parse_qqwry.sh:				Parse qqwry
  python/:						Diectory of python files
	auto_modify_isp.py			Query TaoBao ISP API modify our ISP
	check_isp.py				Check difference between Origin/Mine <IP, ISP>
    clear_ipb.py:				Clean origin ipb file
    convert_location_txt2list.pyCreate Location&Code map
    convert_qqwry_ip2num.py:	Convert ip to INT
    convert_qqwry_loc2id.py:	Convert Loc to ID
	create_as_isp.py			Create <AS, ISP> Mapping
	create_ip_isp.py			Create <IP, ISP> Mapping
	expand_ip.py				Expand cidr to IPs
	get_ip.py					Get Chinese IPs
    ipUtil.py:					Utility functions of IP
	merge_ipb_isp.py			Merge ipb&isp data
	merge_ipb_qqwry.py			Merge ipb&loc data
	parse_aggr.py				Parse aggr.html get <AS, IPs>
	select_cn_ip_as.py			Get Chinese ASes

src/:							Directory of source files


tmp/:							Tempopary files during flow
  as.isp						Mapping of AS&ISP
  cn.as.sum						Statistical Inforomation of Chinese IP
  cn.ip							All Chinese IPs
  cn.ip.expand					All Chinese IPs(expand)
  conflict.ip					IPs which can not match origin IPB
  ip.as							Mapping IP&AS
  ip.as.cn						Mapping IP&AS(China)
  ip.as.expand					Mapping IP&AS(China expand)
  ipb.list:						IPB list from origin ipb
  ipb.list.ips.new				IPR
  ipb.list.new					IPB&Loc
  ip.isp						All IPs from IPB
  ipr							IPR(copy of ipb.list.ips.new)
  location						Mapping Loc&Code
  location.cn 					Mapping Loc&Code(China)
  location.tmp					Tmp file of location list
  qqwry.list:					Parse from qqwry.dat
  qqwry.num.id.list: 			Change Loc from text to Code
  qqwry.num.list:				Change IP from Dotted to Num

result/:						Result of Program
	ipr							Final IPRepository
	location					Loc&Code Map
