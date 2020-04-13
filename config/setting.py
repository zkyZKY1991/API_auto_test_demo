# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 19:27
# @Author   : zky_wind
# @Email    : 475854688@qq.com
# @File     : setting.py
# @Software : PyCharm
import os


class Config:
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试数据路径
    data_path = os.path.join(root_path, "data/test_cases.xlsx")
    # 测试用例地址
    test_path = os.path.join(root_path, "test_cases")
    # 测试报告地址
    report_path = os.path.join(root_path, "report")
    # 判断测试报告地址是否存在，不存在则创建该目录
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    # 测试的log地址
    log_path = os.path.join(root_path, "log")
    if not os.path.exists(log_path):
        os.mkdir(log_path)


class DevConfig(Config):
    # 测试环境的项目域名
    host = "http://120.78.128.25:8766/futureloan"


config = DevConfig()
