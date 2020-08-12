# 다음 증권 스크래핑

import json
import urllib.request as req
# from fake_useragent import UserAgent

headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
    'referer': 'https://finance.daum.net'
}

url = "https://finance.daum.net/api/search/ranks?limit=10"

res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')
print('res', res)

rank_json = json.loads(res)['data']
print(rank_json, '\n')

for elm in rank_json:
    print(type(elm))
