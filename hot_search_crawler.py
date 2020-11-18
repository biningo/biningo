import requests
from lxml import etree

url='https://s.weibo.com/top/summary?cate=realtimehot'
bash_url = 'https://s.weibo.com'
resp = requests.get(url=url)

selector = etree.HTML(resp.text)

urls = selector.xpath('//td[@class="td-02"]/a/@href')
urls = [bash_url+url for url in urls]
titles = selector.xpath('//td[@class="td-02"]/a/text()')
content='### :fire:微博热搜<br>\n'
for url,title in zip(urls[:10],titles[:10]):
    content += '- <a href="'+url+'">'+title+'</a><br>\n'

with open('README.md','w') as f:
    f.write(content)