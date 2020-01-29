# 爬虫练习，从小说网站自动下载小说到txt文件

import requests
import re

url = 'https://book.qidian.com/info/1016572786'
response = requests.get(url)
response.encoding = 'utf-8'  # 设置编码格式
html = response.text  # 接收到的文本信息
# 使用正则表达式获取章节信息，获取开头为<head>，结尾为</head>的内容。参数re.S表示适配不可见字符，如空格
ch = re.findall(r'<head>.*?</head>', html, re.S)  # 类型为字符串
print(ch)
