#!/usr/bin/python
# -*- coding: utf-8 -*-
# Prog: t00ls
# Author: 老锥
# date: 2017-12-06 22:41:15

import sys
import hashlib
import re,requests

session=requests.session()

# 获取登录窗口页面的formhash
# GET /logging.php?action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login HTTP/1.1
# Host: www.t00ls.net
def get_hash():
	url = 'https://www.t00ls.net/logging.php?action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
	headers = {'Host':'www.t00ls.net','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':'https://www.t00ls.net/index.php','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8'}
	session.headers.clear()
	session.headers.update(headers)
	r = session.get(url)
	# 获取formhash
	p = r.text.find('formhash') + len('formhash" value="')
	formhash = r.text[p:p+8]
	return formhash

# 模拟登录并返回登陆弹窗内容
# POST /logging.php?action=login&loginsubmit=yes&floatlogin=yes&inajax=1 HTTP/1.1
# Host: www.t00ls.net
#
# formhash=11111111&referer=https%3A%2F%2Fwww.t00ls.net%2Findex.php&loginfield=username&username=%E8%80%81%E9%94%A5&password=xxxxxxxxxxxxxxx&questionid=0&answer=xxxxxxx&cookietime=2592000
def login(formhash, username, password, questionid, answer):
	url = 'https://www.t00ls.net/logging.php?action=login&loginsubmit=yes&floatlogin=yes&inajax=1'
	data = {
	'formhash':formhash,
	'referer':'https://www.t00ls.net/index.php',
	'loginfield':'username',
	'username':username,
	'password':password,
	'questionid':questionid,
	'answer':answer,
	'cookietime':2592000
	}
	headers = {'Host':'www.t00ls.net','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':'https://www.t00ls.net/index.php','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8'}
	session.headers.clear()
	session.headers.update(headers)
	r = session.post(url, data)
	content = r.text
	# print content
	expression = r'<p>(.*)</p>'
	welcome = re.findall(expression, content)
	print welcome[0]


# Search
# POST /search.php HTTP/1.1
# Host: www.t00ls.net
#
# formhash=11111111&srchtxt=searchtext&srchtype=title&searchsubmit=true&st=on&srchuname=&srchfilter=all&srchfrom=0&before=&orderby=lastpost&ascdesc=desc&srchfid%5B%5D=all
def search(formhash, searchtext):
	url = 'https://www.t00ls.net/search.php'
	data = {
	'formhash':formhash,
	'srchtxt':searchtext,
	'srchtype':'title','searchsubmit':'true','st':'on','srchuname':'','srchfilter':'all','srchfrom':'0','before':'','orderby':'lastpost','ascdesc':'desc','srchfid[]':'all'
	}
	headers = {'Host':'www.t00ls.net','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':'https://www.t00ls.net/search.php','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8'}
	session.headers.clear()
	session.headers.update(headers)
	r = session.post(url, data)
	content = r.text
	# print content 
	expression = r'\d{1}" target="_blank" >(.*)</a>'
	name = re.findall(expression, content)  # all unicode
	for n in name:
		print n

def main():
	formhash = get_hash()
	print '[+] formhash:' + formhash
	username = '用户名'
	print '[+] username:' + username
	password = hashlib.md5('密码').hexdigest()
	print '[+] password:' + password
	q = {'0':'安全提问(未设置请忽略)','1':'母亲的名字','2':'爷爷的名字','3':'父亲出生的城市','4':'您其中一位老师的名字','5':'您个人计算机的型号','6':'您最喜欢的餐馆名称','7':'驾驶执照最后四位数字'}
	questionid = '问题id'
	print '[+] question:' + q.get(questionid)
	answer = '问题答案'
	print '[+] answer:' + answer

	login(formhash, username, password, questionid, answer)

	searchtext = sys.argv[1]
	print '[+] searchtext:' + searchtext
	search(formhash, searchtext)

if __name__ == '__main__':
	main()
