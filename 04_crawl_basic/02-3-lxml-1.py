# lxml 사용기초 스크래핑(1)
# pip install lxml
# pip install requests
# pip install cssselect

import requests
from lxml.html import fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 메인함수
    """

    # 세션 사용
    session = requests.Session()

    # 스크래핑 대상 URL
    response = requests.get("https://naver.com")

    # 신문사 링크 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)

    # 결과 추력
    for name,url in urls.items():
        print(name, url)

def scrape_news_list_page(response):
    urls = {}

    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    for a in root.xpath('//div[@class="thumb_area"]/div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]'):

        extract_contents(a)

        name, url = extract_contents(a)
        urls[name] = url;

    return urls

def extract_contents(dom):

    # 신문사명
    name = dom.xpath('./a')[0].xpath('./img')[0].get('alt')

    # 링크
    link = dom.xpath('./div')[0].xpath('./a')[2].get('href')

    return name, link

# 스크래핑 시작
if __name__ == "__main__":
    main()