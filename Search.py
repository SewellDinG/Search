#!/usr/bin/python
# -*- coding: utf-8 -*-
# Prog: Search
# Author: 老锥
# date: 2017-12-07 16:13:38

import os
import sys
import json
import re,requests
import subprocess
from termcolor import cprint

web = [
'https://wiki.ioin.in/search?word=',
'https://xianzhi.aliyun.com/forum/?keyword=',
'https://api.anquanke.com/data/v1/search?s=',
# 'http://www.freebuf.com/?s=',
'https://www.t00ls.net/search.php',
# 'https://forum.90sec.org/search.php',
]

def geturl(word,url):
	url = url + word
	r = requests.get(url)
	content = r.content
	if word in content or 'title' in content: # chinese?
		cprint('[+] ' + url, "cyan")
		# Sec-News by Phithon
		if 'wiki.ioin.in' in url:
			expression = r'class="visit-color" target="_blank">\s*(.*)\s*</a>'
			name = re.findall(expression, content)
			for n in name:
				print n
		# aliyun
		elif 'xianzhi' in url:
			expression = r'<a class="topic-title" href="/forum/topic/\d*/">\s*(.*)\s*</a>'
			name = re.findall(expression, content)
			for n in name:
				print n
		# anquanke API
		elif 'anquanke' in url:
			name_json = json.loads(str(content))
			name_list = name_json['data']
			for n in name_list:
				print n.get('title') # dic
		# freebuf !fail
		elif 'freebuf' in url:
		 	expression = r'</span>(.*)</a></h4></div>'
		 	name = re.match(expression, content)
		 	for n in name:
		 		pass
	else:
		print '[-] ' + url

def posturl(word, url):
	# t00ls
	if 't00ls' in url:
		# try:
		# 	os.system("python t00ls.py")
		# except Exception as e:
		# 	raise
		INTERPRETER = "/usr/bin/python"
		if not os.path.exists(INTERPRETER):
			log.error("Cannot find INTERPRETER at path \"%s\"." % INTERPRETER)
		processor = "t00ls.py"
		cprint('[+] '+url, "cyan")
		pargs = [INTERPRETER, processor, word]
		child = subprocess.Popen(pargs)
		child.wait()

def main():
	word = sys.argv[1]
	for url in web:
		# get
		if url[-3:] != 'php':
			geturl(word, url)
		# post
		else:
			posturl(word, url)

if __name__ == '__main__':
	main()
