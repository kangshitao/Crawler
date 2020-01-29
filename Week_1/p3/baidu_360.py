# 自动向百度或者360等搜索引擎提交关键词
# https://www.baidu.com/s?wd=搜索内容   使用此url即可关键词搜索
import requests
Keyword = 'Python'
url = 'http://www.baidu.com/s'
try:
    kv = {'wd':Keyword}  # 定义要搜索的关键词为python
    ip = {'user-agent':'Mozilla/5.0'}  # 定义浏览标志，模拟浏览器访问
    r = requests.get(url, params = kv, headers = ip)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
    print(r.text)
except:
    print('连接失败')