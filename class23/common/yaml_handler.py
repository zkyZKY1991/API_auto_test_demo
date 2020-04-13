# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/31 17:31
# @Author   : zky_wind
# @Email    : 475854688@qq.com
# @File     : yaml_handler.py
# @Software : PyCharm
import yaml


class YamlHandler:
    def __init__(self, filename, encoding="utf-8"):
        self.filename = filename
        self.encoding = encoding

    def get_data(self):
        with open(self.filename, encoding=self.encoding) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def set_data(self, data):
        with open(self.filename, encoding=self.encoding) as f:
            yaml.dump(data, f, Allow_unicode=True)


if __name__ == '__main__':
    print("pass")