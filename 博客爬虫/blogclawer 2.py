# -*- coding: UTF-8 -*-
import urllib, os
from bs4 import BeautifulSoup

# 新建文件夹
def mkdir(path):
    isExis = os.path.exists(path)               # 判断文件夹是否存在，不存在则新建
    if not isExis:                              
        os.makedirs(path)

# 获取网页html
def getHtml(url):
    page=urllib.urlopen(url)                    # 访问url返回网页html
    html=page.read()                            
    return html                                 

def save(url):
    html = getHtml(url)
    getImg(html)
# 解析所需html部分
def getImg(html):
    soup = BeautifulSoup(html, "html.parser")
    nexturl = soup.select('.pagingNext')
    next = nexturl[0].get('href')
    print next                                  # 获取下一篇博客链接
    data = soup.select('.articleText')			# 找到对应文档节点
    img = data[0]								# 从list(长度为一)取出对应div下的内容
    imglist = img.find_all('img')				# 找到所有的img
    time = soup.time.get_text()					# 获取tag为<time>里的文本 
    folder = time[0:4]+time[5:7]				# 切割time文件夹和文件命名	
    name = time[0:10]
    mkdir(folder)								# 新建文件夹
    x = 0
    if len(imglist) == 0:						# 判断该篇博客是否有图片，没有则返回
    	save(next)

    else:
        for pic in imglist:						    # 遍历imglist下的<img>
            link = pic.get('src')  					# 获取img的src
            print link
            urllib.urlretrieve(link,'./'+folder+'/'+name+'_'+'%s.jpg' %x)
            x+=1

    print time									# 爬完该篇博客图片后打印时间
    save(next)

save('ameblo.jp/xxx')

