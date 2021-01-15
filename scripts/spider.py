# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2021-1-15 下午7:35
from threading import Thread
from queue import Queue

import time
from lxml import etree
from tools import log, auth
from tools import ua

import requests

from tools.html import to_html
from tools import proxy


class DzSpider(Thread):

    def __init__(self, q: Queue, itemQueue: Queue):
        super().__init__()
        self.queue = q
        self.filter_urls = []  # 用于去重
        self.itemQueue = itemQueue

    def download(self, url, flag):
        resp = requests.get(url, headers={
            'User-Agent': ua.get_ua(),
            'Cookie': auth.auth()}, proxies=proxy.get_proxies()[0]
                            )
        if resp.status_code == 200:
            log.info('GET %s 200 OK' % url)
            html = to_html(resp.content)
            if flag:
                self.parse(html)
            else:
                self.parse_detail(html)
                self.filter_urls.append(url)
        else:
            log.error('Error %s %s ' % (url, resp.status_code))

    def parse(self, html):
        root = etree.HTML(html)
        all_urls = root.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a["href"]/text()')

        for url in all_urls:
            log.info(url)
            self.queue.put((url, False))

    def parse_detail(self, html):
        root = etree.HTML(html)
        # 获取当前页面的数据
        info = {}
        shop_name = root.xpath('//*[@id="basic-info"]/h1/e/text()')
        shop_address = root.xpath('//*[@id="address"]/e/text()')
        phone_number = root.xpath('//*[@id="basic-info"]/p/d/text()')
        print(shop_name, shop_address, phone_number)
        log.debug(info)
        self.itemQueue.put(info)

    def run(self):
        while True:
            try:
                url, flag = self.queue.get(timeout=60)
                log.info('downloading %s' % url)
                self.download(url, flag)
                time.sleep(1)
            except Exception as e:
                log.error(e)
                break
