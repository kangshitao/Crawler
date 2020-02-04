# -*- coding: gbk -*-
import requests
import re

# 获取页面所有信息
def getHTMLText(url):
    try:
        header_con = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'referer': 'https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200201&ie=utf8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'cookie': 'thw=cn; t=f2d428812414303e8426b206f9e171bd; cna=OI21FpOH+CUCAXDvrD3O+wPf; _m_h5_tk=3de1ebade2488ddd9d2cc411d79f5374_1580485435583; _m_h5_tk_enc=ca8f8054dd814ae32dfd8be578ed4174; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&id2=UU6jXwETmE1aMA%3D%3D&nk2=3AE1Sj0l&vt3=F8dBxdsSHEeUlpWmHCQ%3D; lgc=%5Cu5EB7%5Cu4ED5%5Cu6D9B; uc4=id4=0%40U2xuBUNzBAucRqR7eXwg1jME8mws&nk4=0%403nXW9dG9e0zIry7wNzwAQXs%3D; tracknick=%5Cu5EB7%5Cu4ED5%5Cu6D9B; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; mt=ci=17_1; enc=QnqOO1wAin8IBmlVwAzoxphL5Y5mywoRd%2BPprhQ6tdlYPxwpecF5%2FogKZq8fq%2FMoeqmirC5Z%2F%2FvLGI6EQ8J6BA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; v=0; cookie2=1356abcf37b37f8a2e8cb44546bd565d; _tb_token_=e73881383b5ee; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _uab_collina=158056461675700088355949; x5sec=7b227365617263686170703b32223a223931303430663339646432313036373138623165383261386139376431663335434d575231764546454f66527537584c39746a365a526f4d4d6a59794e7a63324d7a6b794e6a7330227d; uc1=cookie14=UoTUOqUNW%2BaVgw%3D%3D; JSESSIONID=17E1CE0694D1FAA87500C33099EC37C8; l=cBMHiv_nQ_absncDBOCZnurza779sIRAguPzaNbMi_5CK6L6d8QOo4_h3Fp6cjWdt1LB4Tn8Nrv9-etkiKy06Pt-g3fP.; isg=BPT0Io6eFhKAwYJfFOqrES5KxbJmzRi3s0Gem45VgX8C-ZRDttwER2G7fTEhAVAP',
        }
        r = requests.get(url, headers=header_con)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('获取失败')
        return ""


# 对每一个页面进行解析
def parsePage(ilt, html):  # 使用正则表达式提取信息
    try:
        '''
        淘宝价格内容显示为："view_price":"127.00" 
        '''
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  # 获取所有价格信息.标点符号需要用转义字符，不然会有特殊含义
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)  # 获取所有商品名称信息
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # 提取出价格信息，用eval函数去掉引号
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])   # 将信息添加到ilt列表中
    except:
        print('')


# 打印商品信息
def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'  # 设置输出模版
    print(tplt.format('Numb', 'Pri ce', 'Name'))  # 打印表头
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


# 定义主函数
def main():
    goods = '书包'
    deepth = 2  # 爬取的页面深度
    start_url = 'https://s.taobao.com/search?q=' + goods

    infoList = []  # 输出结果
    for i in range(deepth):
        try:
            url = start_url + '&s=' + str(44*i)  # 每一页有44个商品
            html = getHTMLText(url)
            print('第{}页内容：{}'.format(i+1, html))
            parsePage(infoList, html)
        except:
            continue   # 若某一页出现异常，则跳过此次循环解析下一页
    printGoodsList(infoList)

if __name__ == '__main__':
    main()

