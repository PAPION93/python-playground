# Get 방식 데이터 통신(2)
# RSS

import urllib.request
import urllib.parse

# 행정안전부 https://www.mois.go.kr
# 행전안전부 RSS API URL
API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []
for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

print(params)

for c in params:
    # get parameter
    param = urllib.parse.urlencode(c)

    url = API + "?" + param

    res_data = urllib.request.urlopen(url).read()

    # response data decoding
    contents = res_data.decode('UTF-8')
    print(contents)