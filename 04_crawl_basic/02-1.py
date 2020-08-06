# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# file url
img_url = 'http://image.dongascience.com/Photo/2020/03/5bddba7b6574b95d37b6079c199d7101.jpg'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = "./04_crawl_basic/test1.jpg"
save_path2 = "./04_crawl_basic/index.html"

# exception
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download Failed')
    print(e)
else:
    # Header Print
    print(header1)
    print(header2)

    # file info
    print(format(file1))
    print(format(file2))
    print()

    print("Success")
