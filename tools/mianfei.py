# -*- coding: utf-8 -*-
# import urllib2
import sys
import os
import json
import random
import time
from pyquery import PyQuery as pq

filePath = 'gui-config.json'
timecount = 0


def getServer():
    print(u'获取服务器信息中……%s' % time.asctime(time.localtime(time.time())))
    # response = urllib2.urlopen('https://www.feiyun.us/code')
    doc = pq('https://www.feiyun.us/code')
    server_info = doc('.col-md-4.feature-box').eq(0).find('.hestia-info p').eq(0).text()
    server_info = server_info.split(u'：')
    server_address = server_info[1].split(u'服务器')[0]
    server_password = server_info[3].split(u'连接密码')[0].split(u'加密')[0]

    print(u'获取服务器成功……%s' % time.asctime(time.localtime(time.time())))
    return {
        "address": server_address.strip(),
        "password": server_password.strip()
    }


def openJson():
    print(u'开始打开配置文件……%s' % time.asctime(time.localtime(time.time())))
    fb = open(filePath, 'r')
    dicts = json.load(fb)
    fb.close()
    print(u'开始打开配置文件成功……%s' % time.asctime(time.localtime(time.time())))
    return dicts


def loadServer(data, server_config):
    print(u'开始写入配置信息……%s' % time.asctime(time.localtime(time.time())))
    data['configs'][0]['server'] = server_config['address']
    data['configs'][0]['password'] = server_config['password']
    fb = open(filePath, 'w')
    fb.write(json.dumps(data, indent=2))
    fb.close()
    print(u'开始写入配置成功……%s' % time.asctime(time.localtime(time.time())))


def restartSS():
    print(u'重启客户端……%s' % time.asctime(time.localtime(time.time())))
    os.system('taskkill /f /t /im Shadowsocks.exe')
    os.system('C:\Users\zj\Downloads\Shadowsocks-4.0.4\Shadowsocks.exe')
    os._exit()


def fun_timer():
    while True:
        restartSS()
        timecount += 1
        randomtime = random.randint(6, 10)
        if timecount > randomtime:
            main()
        time.sleep(60000)


def main():
    server_config = getServer()
    data = openJson()
    loadServer(data, server_config)
    restartSS()
    fun_timer()


main()
