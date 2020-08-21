#던파 아카이브에서 이미 읽어오는걸 한번 더 읽어오기

import pymongo
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

client = MongoClient('localhost', 27017)
db = client.dbsparta

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#
# data = requests.get("http://df.nexon.com/df/info/equipment/view?id=v1czui", headers = headers)

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://df.nexon.com/df/info/equipment#btn')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()

trs = soup.select('#equipmentList > dl')

urls = []
for tr in trs:
    a = tr.select_one('a')
    if a is not None:
        base_url = 'http://df.nexon.com/'
        url = base_url + a['href']
        urls.append(url)


for i in range (0, len(urls)):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(urls[i])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()

    name = soup.select_one('#equipmentList > div.equi_more > div.cardView > div > div > dl > dt > a > span').text
    img_url = soup.select_one('#equipmentList > div.equi_more > div.cardView > div > div > dl > dt > a > img')['src']

    doc = {
        'name': name,
        'img_url': img_url,
    }

    db.epictable.insert_one(doc)
    print(name)