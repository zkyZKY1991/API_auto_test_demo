# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 15:34
# @Author   : zky_wind
# @Email    : 475854688@qq.com
# @File     : run.py
# @Software : PyCharm
import datetime
import os
import unittest

from config.setting import config
from libs import HTMLTestRunnerNew

# 初始一个测试用例加载器
loader = unittest.TestLoader()
# 发现测试用例，并用suite存储
suite = loader.discover(config.test_path, "test*.py")
# 获取当前时间
new_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
# 生成当前测试报告的地址
test_report = os.path.join(config.report_path, "{}_report.html".format(new_time))
# 初始化一个html的运行器
with open(test_report, "wb") as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(f, verbosity=2, title="柠檬班-前程贷接口测试",
                                              description="用来测试前程的注册，登录，充值等接口",
                                              tester="ZKY")
    # 执行测试用例
    runner.run(suite)
