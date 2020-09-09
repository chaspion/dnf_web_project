#던파 아카이브에서 이미 읽어오는걸 한번 더 읽어오기

import pymongo
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

client = MongoClient('mongodb://chaspion:tkfkdgo3@52.79.150.186', 27017)
db = client.dbsparta

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#
# data = requests.get("http://df.nexon.com/df/info/equipment/view?id=v1czui", headers = headers)

# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://dnf.akaib.com/')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# driver.close()




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--single-process")
chrome_options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)
driver.get('https://dnf.akaib.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()




epics = soup.select('#recent-epic > div > ul > li')

for epic in epics:
    time = epic.select_one('span.label.label-primary.pull-left')
    name = epic.select_one('span:nth-child(2) > b > a')
    channel = epic.select_one('span:nth-child(2) > i')
    img_url = epic.select_one('span:nth-child(2) > img')

    if time and name and channel is not None:
        epic_db = {
            'time': time.text,
            'name': name.text,
            'channel': channel.text[:3],
            'channel_name': channel.text[5:8],
            'img_url': img_url['src'],
            #parse string to time to save time data
            # 'date': datetime(2020, time.text[:2], time.text[4:6], time.text[8:10], time.text[11:13], 0)
        }
        db.epics.update(epic_db, epic_db, upsert=True)
        print(time.text, name.text, channel.text[:3], channel.text[5:8])
        # db.epics.delete_many({})