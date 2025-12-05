# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://blog.csdn.net/xindoo?type=blog'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'} 

def addIntro(f):
	txt = '''  
<p align="center">
  <img src="https://github.com/xindoo/xindoo/blob/output/github-contribution-grid-snake.svg"/>
</p>	
<p align="center">
  <img src="https://githubcard.com/xindoo.svg?d=vaqeXVQZ"/>
</p>

<p align="center"> 10+年技术博主，CSDN、华为云、阿里云等社区认证博客专家，2022腾讯云开发者社区年度潜力作者…… </p>  
<p align="center"> 曾在某大厂做过2年运维+1年开发，做过广告引擎，现为某厂资深工程师，拥有丰富的 挖坑 踩坑 填坑 背锅经验 🐶   </p>  
<p align="center"> 擅长Java、Lniux、Redis，对操作系统、网络、编译原理也有涉猎</p>  


''' 
	f.write(txt)

def addProjectInfo(f):
	txt ='''
### 开源项目  
- [eng-practices-cn](https://github.com/xindoo/eng-practices-cn)谷歌工程实践中文版	
- [agentic-design-patterns](https://github.com/xindoo/agentic-design-patterns)谷歌Agent设计模式中文版
- [regex](https://github.com/xindoo/regex)Java实现的正则引擎表达式	
- [redis](https://github.com/xindoo/redis) Redis中文注解版  
- [slowjson](https://github.com/xindoo/slowjson) 用antlr实现的json解析器  
- [leetcode](https://github.com/xindoo/leetcode) 我的Leetcode题解   
   
[查看更多](https://github.com/xindoo/)	 

	''' 
	f.write(txt) 

def addZhuanlanInfo(f):
	txt ='''
### 我的专栏  
- [程序猿进阶](https://blog.csdn.net/xindoo/category_11716954.html)
- [Redis源码剖析](https://blog.csdn.net/xindoo/category_10068113.html)  
- [面试题精选](https://blog.csdn.net/xindoo/category_9991116.html)  
- [高效工程师系列](https://blog.csdn.net/xindoo/category_9287916.html)  
- [Java源码解析](https://blog.csdn.net/xindoo/category_9287770.html)    
- ……

	''' 
	f.write(txt) 


def addBlogInfo(f):  
	http = urllib3.PoolManager(num_pools=5, headers = headers)
	resp = http.request('GET', blogUrl)
	resp_tree = etree.HTML(resp.data.decode("utf-8"))
	# html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
	html_data = resp_tree.xpath(".//article[@class='blog-list-box']")

 
	f.write("\n### 我的博客\n")
	cnt = 0
	for i in html_data: 
		if cnt >= 5:
			break
		# title = i.xpath('./a/text()')[1].strip()
		title = i.xpath("./a//h4/text()")[0].strip()
		url = i.xpath('./a/@href')[0] 
		item = '- [%s](%s)\n' % (title, url)
		f.write(item)
		cnt = cnt + 1
	f.write('\n[查看更多](https://xindoo.blog.csdn.net/)\n')


if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	f.write('<table align="center"><tr>\n')
	f.write('<td valign="top" width="33%">\n')
	addProjectInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="33%">\n')
	addBlogInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="33%">\n')
	addZhuanlanInfo(f)
	f.write('\n</td>\n')
	f.write('</tr></table>\n')
	f.close 

