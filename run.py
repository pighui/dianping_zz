# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2021-1-15 下午7:25
from scripts.spider import DzSpider
from scripts.pipeline import ItemPipeline
from queue import Queue

if __name__ == '__main__':
    q = Queue()
    itemQueue = Queue()
    for i in range(1,51):
        url ="http://www.dianping.com/zhangzhou/ch10/p%s"%str(i)
        q.put((url,True))

    pipeline = ItemPipeline(itemQueue)
    pipeline.start()

    spider = DzSpider(q, itemQueue)
    spider.start()

    spider.join()
    pipeline.join()
    print('--Close Spider---')
