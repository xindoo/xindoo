#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib3
import re
import sys

llmsUrl = 'https://zxs.io/llms.txt'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}


def addIntro(f):
    txt = '''  
<p align="center">
  <img src="https://github.com/xindoo/xindoo/blob/output/github-contribution-grid-snake.svg" alt="GitHub Contribution Snake"/>
</p>	
<p align="center">
  <img src="https://githubcard.com/xindoo.svg?d=vaqeXVQZ" alt="GitHub Stats"/>
</p>

<p align="center"> <strong>AI工具人</strong> | <strong>提示词工程师</strong> | 10+年技术博主，CSDN/华为云/阿里云等社区认证博客专家，2022腾讯云开发者社区年度潜力作者 </p>  
<p align="center"> 曾就职于阿里、小米，现任贝壳资深工程师 | 码龄14年，CSDN 172万+访问量，2.1万+粉丝 </p>  
<p align="center"> 拥有运维、搜索广告、后端业务相关工作经验，擅长Java、Linux、Redis，对AI/Agent、操作系统、网络、编译原理也有涉猎</p>  


''' 
    f.write(txt)


def addProjectInfo(f):
    txt = '''
### 开源项目  
- [agentic-design-patterns](https://github.com/xindoo/agentic-design-patterns)谷歌Agent设计模式中文版
- [eng-practices-cn](https://github.com/xindoo/eng-practices-cn)谷歌工程实践中文版	
- [regex](https://github.com/xindoo/regex)Java实现的正则引擎表达式	
- [redis](https://github.com/xindoo/redis) Redis中文注解版  
- [slowjson](https://github.com/xindoo/slowjson) 用antlr实现的json解析器  
- [leetcode](https://github.com/xindoo/leetcode) 我的Leetcode题解   
   
[查看更多](https://github.com/xindoo/)	 

'''
    f.write(txt)


def addZhuanlanInfo(f):
    txt = '''
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
    http = urllib3.PoolManager(num_pools=5, headers=headers)
    resp = http.request('GET', llmsUrl)
    content = resp.data.decode("utf-8")
    
    # Parse the "## 文章" section
    lines = content.split('\n')
    in_articles_section = False
    articles = []
    
    for line in lines:
        line = line.strip()
        if line == '## 文章':
            in_articles_section = True
            continue
        elif line.startswith('## ') and in_articles_section:
            break
        elif in_articles_section and line.startswith('- ['):
            # Parse the markdown link format: - [title](url)
            match = re.match(r'- \[([^\]]+)\]\(([^)]+)\)', line)
            if match:
                title = match.group(1)
                url = match.group(2)
                articles.append((title, url))
    
    f.write("\n### 我的博客\n")
    cnt = 0
    for title, url in articles:
        if cnt >= 5:
            break
        item = '- [%s](%s)\n' % (title, url)
        f.write(item)
        cnt = cnt + 1
    f.write('\n[查看更多](https://zxs.io/)\n')


if __name__ == '__main__':
    f = open('README.md', 'w', encoding='utf-8')
    try:
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
        print("README.md generated successfully!")
    except Exception as e:
        print(f"Error generating README: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        f.close()
