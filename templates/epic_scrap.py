#던파 홈피 장비사전에서 불러오기

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

from selenium import webdriver

client = MongoClient('localhost', 27017)
db = client.dbsparta

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://df.nexon.com/df/info/equipment#btn')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()

def get_urls():

    trs = soup.select('#equipmentList > dl')
    # old_content > table > tbody > tr:nth-child(2) > td.title > a
    # equipmentList > dl:nth-child(1) > a > dd > p.larea > strong
    # equipmentList > dl:nth-child(1) > a
    # equipmentList > dl:nth-child(2) > a

    urls = []
    for tr in trs:
        a = tr.select_one('a')
        if a is not None:
            base_url = 'http://df.nexon.com/'
            url = base_url + a['href']
            urls.append(url)

    return urls


# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
def insert_star(urls):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(urls)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()

    name = soup.select_one('#equipmentList > div.equi_more > div.cardView > div > div > dl > dt > a > span').text
    img_url = soup.select_one('#equipmentList > div.equi_more > div.cardView > div > div > dl > dt > a > img')['src']
    recent_channel_name = soup.select_one('#equipmentList > div.epicDrop > div > dl:nth-child(1) > dt > span:nth-child(1)').text
    recent_channel = soup.select_one('#equipmentList > div.epicDrop > div > dl:nth-child(1) > dt').text
    recent_time = soup.select_one('#equipmentList > div.epicDrop > div > dl:nth-child(1) > dd')

    doc = {
        'name': name,
        'img_url': img_url,
        'channel_name': recent_channel_name,
        'channel': recent_channel,
        'time': recent_time
    }

    db.epictable.insert_one(doc)
    print('완료!', name)


# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
# def insert_all():
#     db.mystar.drop()  # mystar 콜렉션을 모두 지워줍니다.
#     urls = get_urls()
#     for url in urls:
#         insert_star(url)


### 실행하기
# insert_all()