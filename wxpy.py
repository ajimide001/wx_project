#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import re
import time
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()
DEFAULT_HEADS = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://wx.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.18 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://wx.qq.com/',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}

def unix_13():
    return int(time.time() * 1000)

def unix_17():
    return int(time.time() * 10000000)

class WXPY(object):
    def __init__(self):
        self.s = requests.Session()
        self.s.headers = DEFAULT_HEADS
        self.s.verify = False

    def get_index_url(self):
        index_url = 'https://wx.qq.com/'
        res = self.s.get(index_url)
        # print(res.cookies)

    def get_appid(self):
        appid_url = 'https://res.wx.qq.com/a/wx_fed/webwx/res/static/js/index_ca360ff.js'
        res = self.s.get(appid_url)
        p = re.compile("appid='(.*?)'")
        self.appid = p.search(res.text).group(1)
        print(self.appid)

    def get_qrcode_arg(self):
        qrcode_arg_url = 'https://login.wx.qq.com/jslogin'
        param = {
            'appid':'wx782c26e4c19acffb',
            'fun':'new',
            'lang':'zh_CN',
            'redirect_uri':'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
            '_':unix_13()
        }
        res = self.s.get(qrcode_arg_url,params=param)
        p = re.compile('window.QRLogin.uuid = "(.*?)";')
        self.uuid = p.search(res.text).group(1)
        print('获取UUID成功{}'.format(self.uuid))

    def download_qrcode(self):
        download_url = 'https://login.weixin.qq.com/qrcode/{}'.format(self.uuid)
        res = self.s.get(download_url)
        with open('qrcode.png','wb') as f:
            f.write(res.content)
        print('图片保存成功')

    def login_status(self):
        login_status_url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login'
        param = {
            'loginicon':'true',
            'tip':'0',
            'uuid':self.uuid,
            '_': unix_13()
        }
        for i in range(60):
            res = self.s.get(login_status_url,params=param)
            p = re.compile('window.code=(.*?);')
            code = int(p.search(res.text).group(1))
            if code == 200:
                print('扫码登陆成功')
                p = re.compile('window.redirect_uri="(.*?)";')
                self.redirect_uri = p.search(res.text).group(1)
                return True
            elif code == 408:
                print('等待扫码超时')
            elif code == 201:
                print('等待阻塞201')
            else:
                print('未知错误')
                break
    def set_cookie(self):
        res = self.s.get(self.redirect_uri,allow_redirects=False)
        html = BeautifulSoup(res.text,'lxml')
        skey = html.skey.text
        wxsid = html.wxsid.text
        wxuin = html.wxuin.text
        pass_ticket = html.pass_ticket.text
        self.login_xinxi = {
            'Skey':skey,
            'Sid':wxsid,
            'Uin':wxuin,
            'DeviceID':pass_ticket
        }
        print(self.login_xinxi)
    def get_user(self):
        user_url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?r=1516980473115&seq=0&skey={}'.format(self.login_xinxi['Skey'])
        res = self.s.get(user_url)
        res.encoding = 'utf-8'
        res_json = res.json()
        for i in res_json['MemberList']:
            print(i['UserName'])
            print(i['NickName'])
            print(i['RemarkName'])
        # res = self.s.get(user_url)
        # print(res.encoding)
        # print(res.content)
if __name__ == '__main__':
    wx = WXPY()
    # wx.get_index_url()
    # wx.get_appid()
    wx.get_qrcode_arg()
    wx.download_qrcode()
    flag = wx.login_status()
    if flag:
        wx.set_cookie()
        wx.get_user()
