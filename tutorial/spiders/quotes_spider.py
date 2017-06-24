import time

import requests
import scrapy
import random

from lxml import etree

from tutorial import getProxy

# from ..items import tutorialItem

proxy = getProxy.Proxy()


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://dalian.anjuke.com/sale/',
        ]

        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        headers = {'User-Agent': user_agent}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, method='GET', callback=self.parse)

    def parse(self, response):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        headers = {'User-Agent': user_agent}

        lists = response.body.decode('utf-8')
        selector = etree.HTML(lists)
        area_list = selector.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/span[2]/a')
        # print('lists', lists)
        for area in area_list:
            # print(area)
            try:
                area_han = area.xpath('text()').pop()  # 地点

                url = area.xpath('@href').pop()  # 拼音
                print('url', url)
                # area_url = 'http://dl.lianjia.com/ershoufang/{}/'.format(area_pin)
                yield scrapy.Request(url=url, headers=headers, callback=self.detail_url)
            except Exception as e:
                pass

    def detail_url(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'}
        # print('response', response.body.decode('utf-8'))
        for i in range(1, 100):
            time.sleep(5)
            index = random.randint(1, 100)
            ip = proxy.get_proxy()[index]
            proxy_ip = {'HTTPS': ip}
            url = 'https://dalian.anjuke.com/sale/ganjingzi/p{}/#filtersort'.format(str(i))
            contents = requests.get(url, headers=headers, proxies=proxy_ip)
            contents = etree.HTML(contents.content.decode('utf-8'))
            house_list = contents.xpath('/html/body/div[1]/div[2]/div[4]/ul[1]/li')

            print('house_list', house_list)
            print('次数', i)
            # contents = etree.HTML(contents)


            # house_list = contents.xpath('/html/body/div[4]/div[1]/ul/li/div[1]')
