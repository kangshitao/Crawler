# 从网站自动下载图片
import requests
import os

url = 'https://desk-fd.zol-img.com.cn/t_s960x600c5/g5/M00/0E/04/ChMkJl4lGF6Iay2pAAXEJ7k8RI0AAweGgOVC0UABcQ_106.jpg'
root = 'picture//'
path = root + url.split('/')[-1]  # 定义文件保存路径
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)  # r.content为二进制文件
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
