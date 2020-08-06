# urlopen

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ['./04_crawl_basic/test1.jpg', './04_crawl_basic/index.html']

# 다운로드 리소스 url
target_url = ['http://image.dongascience.com/Photo/2020/03/5bddba7b6574b95d37b6079c199d7101.jpg',
              'http://google.com']

for i, url in enumerate(target_url):
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'. format(i, response.info()))
        print('Http Status Code {}'. format(response.getcode()))
        print()

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download Fail")
        print("Http Error Code: ", e.code)
    except URLError as e:
        print("Download Fail")
        print("URL Error Reason : ", e.reason)
    else:
        print()
        print("Download Succeed.")
