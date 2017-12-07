#!/usr/bin/python
# -*- coding: utf-8 -*-
# Prog: 90sec
# Author: 老锥
# date:2017-12-07 14:35:38

import sys
import hashlib
import re,requests

session=requests.session()

# 获取登录页面的loginhash和formhash
# POST /member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash=LK8QH&inajax=1 HTTP/1.1
# Host: forum.90sec.org
def get_hash():
	url = 'https://forum.90sec.org/member.php?mod=logging&action=login&infloat=yes&frommessage&inajax=1&ajaxtarget=messagelogin'
	headers = {'Host':'forum.90sec.org','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':'https://forum.90sec.org/','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8'}
	session.headers.clear()
	session.headers.update(headers)
	r = session.get(url)
        #获取loginhash
        p=r.text.find('loginhash')+len('loginhash=')
        loginhash=r.text[p:p+5]
        #获取formhash
        p=r.text.find('formhash')+len('formhash" value="')
        formhash=r.text[p:p+8]
        return (loginhash,formhash)

# 模拟登录并返回登陆弹窗内容
# POST /member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash=LK8QH&inajax=1 HTTP/1.1
# Host: forum.90sec.org
#
# formhash=11111111&referer=https%3A%2F%2Fforum.90sec.org%2F&loginfield=username&username=%C0%CF%D7%B6&password=xxxxxxxxxxxxxxx&questionid=0&answer=xxxxxxx
def login(loginhash, formhash, username, password, questionid, answer):
	url = 'https://forum.90sec.org/member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash='+loginhash+'&inajax=1'
	data = {
	'formhash':formhash,
	'referer':'https://forum.90sec.org/',
	'loginfield':'username',
	'username':username,
	'password':password,
	'questionid':questionid,
	'answer':answer,
	}
	headers = {'Host':'forum.90sec.org','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Referer':'https://forum.90sec.org/','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Upgrade-Insecure-Requests':'1'}
	session.headers.clear()
	session.headers.update(headers)
	r = session.post(url, data)
	content = r.text
	print content

def main():
	(loginhash,formhash) = get_hash()
	print '[+] loginhash,formhash:' + loginhash + ',' + formhash
	username = '用户名'
	print '[+] username:' + username
	password = hashlib.md5('密码').hexdigest()
	print '[+] password:' + password
	q = {'0':'安全提问(未设置请忽略)','1':'母亲的名字','2':'爷爷的名字','3':'父亲出生的城市','4':'您其中一位老师的名字','5':'您个人计算机的型号','6':'您最喜欢的餐馆名称','7':'驾驶执照最后四位数字'}
	questionid = '问题id'
	print '[+] question:' + q.get(questionid)
	answer = '问题答案'
	print '[+] answer:' + answer

	login(loginhash, formhash, username, password, questionid, answer)

if __name__ == '__main__':
	main()
