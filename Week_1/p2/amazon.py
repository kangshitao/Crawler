# 亚马逊网站的内容爬取
import requests
url = 'https://www.amazon.cn/dp/B07J3FWS5J/ref=sr_1_3?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=iphone&qid=1580277354&rnid=2044974051&s=wireless&sr=1-3'
try:
    kv = {'user-agent':'Mozilla/5.0'}  # 定义浏览标志，模拟浏览器访问
    r = requests.get(url, headers = kv)
    r.raise_for_status()  # 状态码，200表示正常连接，其他数表示出现异常。返回非200的数时，抛出异常
    r.encoding = r.apparent_encoding  # 设置编码信息
    print(r.text)
except:
    print('连接失败')
