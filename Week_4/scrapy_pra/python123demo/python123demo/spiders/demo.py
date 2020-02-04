# -*- coding: utf-8 -*-
import scrapy

# 更改配置信息，编写将网页内容写入文件的例子
class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']  # 定义的域名，暂时无用
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open (fname, 'wb') as f:
            f.write(response.body)  # 将网页内容写入文件
        self.log("Saved file %s." % fname)
