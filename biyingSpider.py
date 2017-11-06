#coding:utf-8
import requests
import re
import time
import hashlib
from var_dump import *
def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()

url = 'https://baidu.com/'
con = requests.get(url)
content = con.text

reg = "www.baidu.com/img/.*?.png"
a = re.findall(reg, content, re.S)
url = "http://" + a[0]

f0 = open('baidu.html', 'a+')
f0.write(url + '\n')

read = requests.get(url)
f = open('%s.jpg' % create_id(), 'wb')
f.write(read.content)
f.close()
