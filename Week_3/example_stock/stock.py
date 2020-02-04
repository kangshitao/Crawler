import requests
from bs4 import BeautifulSoup
import re
import traceback


def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()

        # apparent_encoding 解析编码时比较耗时，定向爬虫可以直接手动赋值编码
        #r.encoding = r.apparent_encoding
        r.encoding = code
        return r.text
    except:
        print('获取失败')
        return ""


# 获取所有股票的id信息
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')  # 发现网址内所有股票信息都是存在a标签内
    for i in a:
        try:
            href = i.attrs['href']  # 从a标签中找到href属性
            lst.append(re.findall(r'[s][hz]\d{6}', href[0]))
        except:
            continue  #　由于并不是所有的ａ标签都是股票信息，所以如果没找到就继续下一个


#获取每只股票的信息
def getStockInfo(lst, stockURL, fpath):
    count = 0  # 用于生成动态进度条

    for stock in lst:
        url = stockURL + stock + '.html'  # 获取单支股票的url链接
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            infoDict = {}  # 存储股票信息
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})  # 根据百度股市通网页股票内容提取相应的股票信息
            name = stockInfo.find_all(attrs={'class':'stock-bets'})[0]
            infoDict.update({'股票信息':name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding="utf-8") as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度:{:.2f}%'.format(count*100/len(lst)), end='')  # 打印进度

        except:
            # traceback.print_exc()  # 输出异常信息
            count = count + 1
            print('\r当前速度:{:.2f}%'.format(count * 100 / len(lst)), end='')  # 打印进度
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html/'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)  # 获取股票列表
    getStockInfo(slist, stock_info_url, output_file)  # 根据获得的股票列表信息，获取单支股票的信息


if __name__ == '__main__':
    main()