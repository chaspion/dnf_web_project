import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#
# data = requests.get("https://dunfaoff.com/ranking.df", headers = headers)
# soup = BeautifulSoup(data.text, 'html.parser')


# client = MongoClient('mongodb://chaspion:tkfkdgo3@13.125.243.111', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta


#페이지1 크롤링
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=101%2C207&max=100&min=0&order_name=rarity&order_type=desc')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()



item_info = soup.select('#searchList > tr')
for items in item_info:
    name = items.select_one('td.name > div:nth-child(2) > span.item_c8').text
    img_url = items.select_one('td.name > div.boxaxis.ico > em > img')['src']
    item_url = 'http://df.nexon.com/df' + items['data-link'][3:] + '&page=1&is_limit=&filter=207&max=100&min=0&order_name=rarity&order_type=desc'

    mythic_db = {
        'name': name,
        'img_url': img_url,
        'item_url': item_url,
        'count': 0
    }

    db.mythic.insert_one(mythic_db)
    db.mythic.update(mythic_db, mythic_db, upsert=True)


#페이지2 크롤링
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=102%2C207&max=100&min=0&order_name=rarity&order_type=desc')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()



item_info = soup.select('#searchList > tr')
for items in item_info:
    name = items.select_one('td.name > div:nth-child(2) > span.item_c8').text
    img_url = items.select_one('td.name > div.boxaxis.ico > em > img')['src']
    item_url = 'http://df.nexon.com/df' + items['data-link'][3:] + '&page=1&is_limit=&filter=207&max=100&min=0&order_name=rarity&order_type=desc'

    mythic_db = {
        'name': name,
        'img_url': img_url,
        'item_url': item_url,
        'count': 0
    }

    db.mythic.insert_one(mythic_db)
    db.mythic.update(mythic_db, mythic_db, upsert=True)


#페이지3 크롤링
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=103%2C207&max=100&min=0&order_name=rarity&order_type=desc')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()



item_info = soup.select('#searchList > tr')
for items in item_info:
    name = items.select_one('td.name > div:nth-child(2) > span.item_c8').text
    img_url = items.select_one('td.name > div.boxaxis.ico > em > img')['src']
    item_url = 'http://df.nexon.com/df' + items['data-link'][3:] + '&page=1&is_limit=&filter=207&max=100&min=0&order_name=rarity&order_type=desc'

    mythic_db = {
        'name': name,
        'img_url': img_url,
        'item_url': item_url,
        'count': 0
    }

    db.mythic.insert_one(mythic_db)
    db.mythic.update(mythic_db, mythic_db, upsert=True)

