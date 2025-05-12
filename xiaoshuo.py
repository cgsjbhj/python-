import requests
from lxml import etree
from time import sleep
url = 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/1.html'
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
}
for i in range(1,10):
    # 发送请求
    resp = requests.get(url,headers = header)
    resp.encoding = 'utf-8'
    # 响应信息
    # print(resp.text)
    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]

    # 保存
    with open('斗罗大陆.txt','a',encoding='utf-8')as f:
        f.write(title+'\n\n'+info+'\n\n')
    
    next_url = e.xpath('//tr/td[2]/a/@href')[0]
    url = 'https://dldl1.nsbuket.cc'+next_url
    print(url)
    sleep(1)
print('爬取完毕')