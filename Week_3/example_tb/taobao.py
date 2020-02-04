# -*- coding: gbk -*-
import requests
import re

# ��ȡҳ��������Ϣ
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
        print('��ȡʧ��')
        return ""


# ��ÿһ��ҳ����н���
def parsePage(ilt, html):  # ʹ��������ʽ��ȡ��Ϣ
    try:
        '''
        �Ա��۸�������ʾΪ��"view_price":"127.00" 
        '''
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  # ��ȡ���м۸���Ϣ.��������Ҫ��ת���ַ�����Ȼ�������⺬��
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)  # ��ȡ������Ʒ������Ϣ
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # ��ȡ���۸���Ϣ����eval����ȥ������
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])   # ����Ϣ��ӵ�ilt�б���
    except:
        print('')


# ��ӡ��Ʒ��Ϣ
def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'  # �������ģ��
    print(tplt.format('Numb', 'Pri ce', 'Name'))  # ��ӡ��ͷ
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


# ����������
def main():
    goods = '���'
    deepth = 2  # ��ȡ��ҳ�����
    start_url = 'https://s.taobao.com/search?q=' + goods

    infoList = []  # ������
    for i in range(deepth):
        try:
            url = start_url + '&s=' + str(44*i)  # ÿһҳ��44����Ʒ
            html = getHTMLText(url)
            print('��{}ҳ���ݣ�{}'.format(i+1, html))
            parsePage(infoList, html)
        except:
            continue   # ��ĳһҳ�����쳣���������˴�ѭ��������һҳ
    printGoodsList(infoList)

if __name__ == '__main__':
    main()

