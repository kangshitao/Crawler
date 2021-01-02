import requests
import re
import os
from pathlib import Path
import time
import datetime
from tqdm import tqdm

import urllib3
urllib3.disable_warnings()  # 禁用证书认证和警告

"""
Created on January 1st, 2021
@author: Kangshitao
"""

# 获取每季中每集的m3u8地址,每季只获取一次即可
def get_m3u8_list(url,S):
    req = requests.get(url)
    req.encoding = 'utf-8'
    html = req.text
    res_url = re.findall(r'https:\\/\\/youku.com-youku.net.*?index.m3u8', html, re.S)
    m3u8list = []
    for i in range(len(res_url)):
        url = res_url[i].split('\\')
        # m3u8文件下载下来以后，文件内容才是真正的m3u8地址，这里为了方便起见，手动构建url
        # 真正的url多了'1000k/hls',这里手动添加上
        m3u8list.append(''.join(url[:-1])+'/1000k/hls/index.m3u8')
        print(m3u8list[i])
    print('第{}季m3u8地址获取完毕'.format(S))
    return m3u8list


# 下载ts文件
def download(m3u8_list,base_path,S):  # base_path: "F://Shameless//",S表示当前季数
    print('下载m3u8文件...')
    url = base_path+'Shameless_'+'S'+str(S)  # F://Shameless//Shameless_S1
    path = Path(url)
    # 如果文件夹不存在，则创建
    if not path.is_dir():
        os.mkdir(url)
    for i in range(len(m3u8_list)):
        print('正在下载第{}集...'.format(i+1))
        start = datetime.datetime.now().replace(microsecond=0)
        time.sleep(1)  # sleep一秒
        ts_urls = []  # 保存每一集的ts文件的真实url
        m3u8 = requests.get(url=m3u8_list[i])
        content = m3u8.text.split('\n')
        for s in content:
            if s.endswith('.ts'):
                ts_url = m3u8_list[i][:-10] + s.strip('\n') # 生成ts文件的真实url
                ts_urls.append(ts_url)
        download_ts(ts_urls,down_path=url+'//'+"E"+str(i+1)+'.ts')  # 根据ts的url下载每集的ts文件
        end = datetime.datetime.now().replace(microsecond=0)
        print('耗时：%s' % (end - start))
        print('第{}集下载完成...'.format(i+1))


# 根据ts下载链接下载文件
def download_ts(ts_urls,down_path):
    file = open(down_path, 'wb')
    for i in tqdm(range(len(ts_urls))):
        ts_url = ts_urls[i]  # 例:https://youku.com-youku.net/20180626/14084_f3588039/1000k/hls/80ed70a101f861.ts
        time.sleep(1)
        try:
            response = requests.get(url=ts_url, stream=True, verify=False)
            file.write(response.content)
        except Exception as e:
            print('异常请求：%s' % e.args)
    file.close()


if __name__ == '__main__':
    savefile_path = 'F://Shameless//'
    section_url = ['http://www.tv3w.com/dushiqinggan/wuchizhitudiyiji/5-1.html',
                   'http://www.tv3w.com/dushiqinggan/wuchizhitudierji/3-1.html',
                   'http://www.tv3w.com/dushiqinggan/wuchizhitudisanji/4-1.html',
                   'http://www.tv3w.com/dushiqinggan/wuchizhitudisiji/4-1.html',
                   'http://www.tv3w.com/dushiqinggan/wuchizhitudiwuji/7-1.html',
                   'http://www.tv3w.com/dushiqinggan/wuchizhitudiliuji/7-1.html',
                   'http://www.tv3w.com/dushiqinggan/wuchizhitudiqiji/6-1.html']
    for i in range(len(section_url)):
        print('开始下载第{}季...'.format(i+1))
        episode_url = get_m3u8_list(url=section_url[i],S=i+1) # 获取每季中每一集的m3u8地址
        download(episode_url,savefile_path,i+1)    # 下载每一季的ts文件并拼接
    print('done')