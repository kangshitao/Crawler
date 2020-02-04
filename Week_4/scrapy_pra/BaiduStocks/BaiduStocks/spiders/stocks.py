# -*- coding: utf-8 -*-
import scrapy
import re
# 同样使用获取股票信息的例子。从东方财富网获取股票的代码信息，然后到百度股票查找并下载单支股票的信息保存到文件


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/center/gridlist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]\d{6}',href)[0]  # 获取股票代码
                url = "https://gupiao.baidu.com/stock/" + stock + '.html'  # 生成百度单支股票的url
                yield scrapy.Request(url, callback=self.parse_stock)  # 重新提交request请求
            except:
                continue


    def parse_stock(self,response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*<\dt>', keyList[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key] = val
        infoDict.update(
            {'股票名称':re.findall(r'\s.*\(', name)[0].spilt()[0] + re.findall(r'\>.*\<', name)[0][1:-1]}
        )
        yield infoDict