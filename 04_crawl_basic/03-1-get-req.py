# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청(엔카)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 정보 출력
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('read : {}'.format(mem.read(100).decode('utf-8')))
print('parse1 : {}'.format(urlparse('http://www.encar.co.kr?test=test')))
print('parse2 : {}'.format(urlparse('http://www.encar.co.kr?test=test').query))

# 기본 요청 테스트(ipify)
API = "https://api.ipify.org"

# Get 방식 Parameter 
values = {
    'format' : 'json'
}

print('before param : {}' .format(values))
params = urllib.parse.urlencode(values)
print('after param : {}' .format(params))

# URL Create
URL = API + "?" + params
print("requet URL = {}".format(URL))

# get
data = urllib.request.urlopen(URL).read()

# data encode
text = data.decode('UTF-8')
print("response : {}".format(text))