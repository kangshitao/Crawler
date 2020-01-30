# 中国大学排名定向爬虫

import requests
from bs4 import BeautifulSoup
import bs4


# 获取网页文本内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


# 将文本内容提取到列表中
def fileUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children: # 每一个大学的信息都包含在tbody中的tr标签中
        if isinstance(tr, bs4.element.Tag):  # 判断tr是否是标签类型
            tds = tr('td')  # 等价于tr.find_all('td').查找tr中的td标签。返回类型为list
            # 将每个大学信息的前四项信息作为list加入ulist
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


# 输出正确格式的内容
def printUnivList(ulist, num):
    tplt = '{0:^6}\t{1:{4}^10}\t{2:^6}\t{3:^6}'  # {4}表示用format中的第四个变量填充.^6表示居中对齐，占六位
    # chr(12288)表示中文字符大小的空格.因为输出时占不满时用空格填充，中英文空格符大小不一致导致显示会“错位”
    print(tplt.format('排名', '学校名称', '省市', '总分', chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


# 定义主函数
def main():
    uinfo = []  # 存放大学排名信息
    url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fileUnivList(uinfo, html)
    printUnivList(uinfo, 20)

if __name__ == '__main__':
    main()