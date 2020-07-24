# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re
 
http = urllib3.PoolManager(num_pools=5, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'})
 
resp = http.request('GET', 'https://xindoo.blog.csdn.net/')

resp_tree = etree.HTML(resp.data.decode("utf-8"))
html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
f = open('README.md', 'w+')
f.write("## 我的博客\n")

cnt = 0
for i in html_data: 
	if cnt >= 10:
		break
	title = i.xpath('./a/text()')[1].strip()
	url = i.xpath('./a/@href')[0] 
	txt = '- [%s](%s)\n' % (title, url)
	f.write(txt)
	cnt = cnt + 1
f.close
   