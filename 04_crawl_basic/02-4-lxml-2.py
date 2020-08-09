# lxml 사용기초 스크래핑(2)

import requests
import lxml.html

def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 메인함수
    """

    # 스크래핑 대상 URL
    response = requests.get("https://naver.com")

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 추력
    for url in urls:
        print(url)

        # 파일 쓰기
        # 생략

def scrape_news_list_page(response):
    urls = []

    root = lxml.html.fromstring(response.content)

    for a in root.cssselect('.thumb_area .thumb_box a.thumb'):
        url = a.get('href')
        urls.append(url)

    return urls

# 스크래핑 시작
if __name__ == "__main__":
    main()