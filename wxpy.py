#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests

DEFAULT_HEADS = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://wx2.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.18 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://wx2.qq.com/',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}



class WXPY(object):
    def __init__(self):
        self.s = requests.Session()
        self.s.headers = DEFAULT_HEADS

    def get_index_url(self):
        index_url = 'https://wx.qq.com/'
        res = self.s.get(index_url)
        print(res.text)


if __name__ == '__main__':
    wx = WXPY()
    wx.get_index_url()
