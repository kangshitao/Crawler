# 使用ip138网站，自动查询ip地址的归属地
import requests
import re
url = 'http://www.ip138.com/iplookup.asp?ip='
try:
    r = requests.get(url+'202.204.80.112')
    r.encoding = r.apparent_encoding
    inf = re.findall(r'您查询的IP.*?</li></ul></td>', r.text, re.S)[0]  # 提取信息，默认返回类型为list
    inf = inf.replace('</tr>', '\n')  # 简单清洗数据,使用replace方法，str.replace(a,b)意为将字符串str中的所有a替换为b
    print(r.url)
    print(inf)
except:
    print('爬取失败')
