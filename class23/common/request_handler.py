# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/30 15:36
# @Author   : zky_wind
# @Email    : 475854688@qq.com
# @File     : request_handler.py
# @Software : PyCharm
import requests


class RequestHandler:
    """封装一个request的处理器"""
    def __init__(self):
        self.session = requests.session()

    def visit(self, method, url, headers=None, data=None, **kwargs):
        """传入请求方法，url地址等，返回一个json格式的响应体"""
        req = self.session.request(method, url, headers=headers, data=data, **kwargs)
        try:
            return req.json()
        except ValueError as e:
            print("返回的不是json格式")

    def close_session(self):
        """关闭session会话"""
        self.session.close()
