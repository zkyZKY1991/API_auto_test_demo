# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 15:35
# @Author   : zky_wind
# @Email    : 475854688@qq.com
# @File     : logger_handler.py
# @Software : PyCharm
import datetime
import logging
import os

from config.setting import config


class LoggerHandler(logging.Logger):
    """封装一个logger的类，主要用来输出log信息，并可以存储在特定位置，方便查看"""

    def __init__(self, logger_name='root', level_name="DEBUG", filename=None,
                 format="%(filename)s-%(lineno)d-%(name)s-%(asctime)s-日志信息：%(message)s"):
        # 初始化一个logger的加载器
        super().__init__(logger_name)
        # 设置一个加载器的等级
        self.setLevel(level_name.upper())
        # 创建一个处理器的格式
        fmt = logging.Formatter(format)
        # 判断filename是否为空
        if filename:
            # 获取一个文件处理器
            file_handler = logging.FileHandler(filename, encoding='utf_8')
            # 设置处理器的等级
            file_handler.setLevel(level_name.upper())
            # 设置处理器的输出格式
            file_handler.setFormatter(fmt)
            # 添加处理器
            self.addHandler(file_handler)
        # 获取一个控制台的处理器
        console_handler = logging.StreamHandler()
        # 设置处理器等级
        console_handler.setLevel(level_name.upper())
        # 设置处理器的输出格式
        console_handler.setFormatter(fmt)
        # 添加处理器
        self.addHandler(console_handler)


# 获取当前的日期
new_time = datetime.datetime.now().strftime('%Y_%m_%d')
# 创建一个log.txt的路径
filename = os.path.join(config.log_path, '{}_log.txt'.format(new_time))
# 实例化LoggerHandler
logger = LoggerHandler('tester', filename=filename)

if __name__ == '__main__':
    logger_handler = LoggerHandler('tester', "info")
    logger_handler.info("hello")
    logger_handler.debug('world')
