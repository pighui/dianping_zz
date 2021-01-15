# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2021-1-15 下午7:34

import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler

# 日志
logger = logging.getLogger('msj-spider')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt='[%(asctime)s %(name)s] %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
io_handler = StreamHandler()
io_handler.setLevel(logging.DEBUG)
io_handler.setFormatter(formatter)

file_handler = TimedRotatingFileHandler('dazhong-spider.log',
                                        encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(io_handler)
logger.addHandler(file_handler)


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)


def error(msg):
    logger.error(msg)
