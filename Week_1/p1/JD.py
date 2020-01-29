# 爬取京东商城页面信息
import requests
url = 'https://item.jd.com/100008348548.html'
try:
    r = requests.get(url)
    r.raise_for_status()  # 状态码，200表示正常连接，其他数表示出现异常。返回非200的数时，抛出异常
    r.encoding = r.apparent_encoding  # 编码信息
    print(r.text)
except:
    print('连接失败')
