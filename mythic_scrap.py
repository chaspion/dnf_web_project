import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

# client = MongoClient('mongodb://chaspion:tkfkdgo3@13.125.243.111', 27017)

# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('http://df.nexon.com/df/info/equipment/search?page=2&is_limit=&filter=207&max=100&min=0&order_name=rarity&order_type=desc')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# #searchList > tr:nth-child(1) > td.name > div:nth-child(2)
# item_info = soup.select('#searchList')

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get("https://dunfaoff.com/ranking.df", headers = headers)
soup = BeautifulSoup(data.text, 'html.parser')

mythics = ['가네샤의 영원한 가호', '결속의 체인 플레이트', '고대 심연의 로브', '군신의 마지막 갈망', '길 방랑자의 물소 코트',
           '낭만적인 선율의 왈츠', '대 마법사 [???]의 로브', '대제사장의 예복', '또다른 시간의 흐름', '라이도 : 질서의 창조자',
           '사탄 : 분노의 군주', '새벽을 녹이는 따스함', '생사를 다스리는 그림자의 재킷', '선택이익', '세상을 삼키는 분노', '수석 집행관의 코트',
           '숙명을 뒤엎는 광란', '시간을 거스르는 자침', '아린 고통의 비극', '영명한 세상의 순환', '영원을 새긴 바다', '영원한 나락의 다크버스',
           '영원히 끝나지 않는 탐구', '운명을 거스르는 자', '원시 태동의 대지', '웨어러블 아크 팩', '작열하는 대지의 용맹',
           '종말의 역전', '지고의 화염 - 이프리트', '차원을 관통하는 초신성', '천상의 날개', '천지에 울려퍼지는 포효', '최후의 전술', '트로피카 : 드레이크', '플라즈마 초 진공관',]


db.jobs.delete_many({})
db.jobs.insert_one({'job': '검신', 'class': '귀검사', 'gender': 'M', 'type': 'S'})

urls = []
types = []
for i in range (0, len(job)):
    for j in range(1, 5):
        base_url_1 = 'https://api.neople.co.kr/df/servers/'
        base_url_2 = '&jobGrowName='
        base_url_3 = '&gender='
        base_url_4 = '&page='
        url = base_url_1 + job[i]['class'] + base_url_2 + job[i]['job'] + base_url_3 + job[i]['gender'] + base_url_4 + str(j)
        urls.append(url)
        types.append(job[i]['type'])

db.mythics.delete_many({})
for i in range(0, len(urls)):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(urls[i], headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    char_info = soup.select('#back > div > div.col-sm-12.col-md-12.col-xl-8.col-lg-8 > div > div:nth-child(4) > div')
    for info in char_info:
        server_id = info['server']
        char_id = info['characterid']
        point = info.select_one('#div_damage > b:nth-child(1)').text
        name = info.select_one('#div_rank > b:nth-child(3)').text
        job = urls[i][56:-16].replace('%20', ' ')
        type = types[i]
        print(server_id, char_id, point, name, job, type)

        char_db = {
            'char_id': char_id,
            'server_id': server_id,
            'rank_point': point,
            'char_name': name,
            'job': job,
            'type': type
        }

        db.rank.insert_one(char_db)
        db.rank.update(char_db, char_db, upsert=True)