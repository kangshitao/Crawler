# beautiful soup4使用练习
import requests
import re
from bs4 import BeautifulSoup

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')  # 用html解释器解释demo
#print(soup.prettify())  # 此时输出的是html格式的文本内容。prettify函数能够自动添加换行符
print(soup)
print(soup.title, soup.a)  # 当有多个标签时，只返回第一个标签的信息
print(soup.a.name, soup.a.parent.name)  # 返回标签的名字
print(soup.a.attrs)  # 返回标签的属性(位于<>括号里面的内容)，返回类型为字典
print(soup.a.attrs['href'])
print(soup.a.string)  # 返回a标签中没有位于<>括号里面的内容，即在页面上显示出来的内容

# 遍历标签树的标签内容.包括上行遍历，下行遍历，和平行遍历三种
print('遍历标签：')
print(soup.head.contents)

print('查找某一个标签：')
print(soup.find_all('a'))  # 查找所有a标签.find_all有五个参数，详情参见手册.可以用soup('a')代替soup.find_all('a')
print('查找所有标签：')
for tag in soup.find_all(True):  # 查找所有标签
    print(tag.name)

print('使用正则表达式查找：')
for tag in soup.find_all(re.compile('b')):  # 使用正则表达式查找所有含有b的标签
    print(tag.name)

print(soup.find_all(string = 'Basic Python'))  # 查找不在<>括号里面的内容
