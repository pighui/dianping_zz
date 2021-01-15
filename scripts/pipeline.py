# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2021-1-15 下午7:35
import csv
import sqlite3
from threading import Thread

from tools import log


class ItemPipeline(Thread):
    def __init__(self, itemQueue):
        super().__init__()
        self.queue = itemQueue
        self.csv_filename = 'zhangzhou.csv'
        self.existed_header = False

    def save(self, **item):
        with open(self.csv_filename, 'a', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=item.keys())
            if not self.existed_header:
                writer.writeheader()
                self.existed_header = True
            writer.writerow(item)
        log.info('保存OK', item)
        return item

    def run(self):
        while True:
            try:
                item = self.queue.get(timeout=60)
                self.save(**item)
            except:
                break
