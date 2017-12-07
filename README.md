# Search

碰到想要复现的漏洞，往往会去各大平台搜索相关信息；

打开t00ls，打开90，打开安全客，打开wiki，打开各位师傅的博客...

然后再搜索...费时间，费力气，所以为自己写了个脚本；

## Usage

下载依赖：

```
pip install -r requirements.txt
```

脚本只是简单使用 **sys.argv[1]** 来获取一个参数，没有帮助文档：

```
➜  Search python Search.py CVE-2017-11882  

[+] https://wiki.ioin.in/search?word=CVE-2017-11882
CVE-2017-11882漏洞分析、利用及动态检测
CVE-2017-11882利用

[+] https://xianzhi.aliyun.com/forum/?keyword=CVE-2017-11882
CVE-2017-11882 漏洞分析
微软Offcie CVE-2017-11882漏洞复现

[+] https://api.anquanke.com/data/v1/search?s=CVE-2017-11882
Office公式编辑器漏洞（<em>CVE</em>-<em>2017</em>-<em>11882</em>）已遭利用
11月27日 - 每日安全知识热点
<em>CVE</em>-<em>2017</em>-<em>11882</em>漏洞分析、利用及动态检测
Microsoft Office内存损坏漏洞（<em>CVE</em>–<em>2017</em>–<em>11882</em>)分析
微软如何手工修复Office Equation内存破坏漏洞（<em>CVE</em>-<em>2017</em>-<em>11882</em>）
11月21日 - 每日安全知识热点
<em>CVE</em>-<em>2017</em>-<em>11882</em>：微软Office内存损坏漏洞导致远程命令执行

[+] https://www.t00ls.net/search.php
[+] formhash:12345678
[+] username:老锥
[+] password:abcdefghijklmnopqistuvwxyz
[+] question:0
[+] answer:xxxxxxxx
欢迎您回来 注册会员 老锥
[+] searchtext:CVE-2017-11882
问一下 关于office CVE-2017-11882漏洞利用的问题
投稿文章：Office CVE-2017-11882实战免杀
Office CVE-2017-11882实战免杀 ---转自junay
CVE-2017-11882 POC
```

## Category

公开的这个脚本带的这几个网站涵盖了几种情况：

`wiki.ioin.in` 和 `xianzhi.aliyun.com` 属一类：不需要登陆，利用 **get+关键词** 来搜索；

`api.anquanke.com/data/v1/search?s=` 安全客：搜索调用的 **API**，主页面看不到源代码，需要找到API的位置，同样利用 **get+关键词** 来搜索；

`www.t00ls.net` 和 `forum.90sec.org` 属一类：需要**登陆**，利用 **post+formhash+关键词** 来搜索；

note：

t00ls 和 90sec 均属于discuz，不过登陆都不需要验证码，而且 t00ls 登陆不需要 **loginhash**；

t00s 注册会员以上级别免费，新手上路每进行一次搜索将扣除 TuBi 1；