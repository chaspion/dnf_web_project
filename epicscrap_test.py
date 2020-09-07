import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

# client = MongoClient('mongodb://chaspion:tkfkdgo3@13.125.243.111', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get("https://dunfaoff.com/ranking.df", headers = headers)
soup = BeautifulSoup(data.text, 'html.parser')

db.jobs.delete_many({})
db.jobs.insert_one({'job': '검신', 'class': '귀검사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '다크로드', 'class': '귀검사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '블러드%20이블', 'class': '귀검사', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '인다라천', 'class': '귀검사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '악귀나찰', 'class': '귀검사', 'gender': 'M', 'type': 'D'})
#
# db.jobs.insert_one({'job': '네메시스', 'class': '귀검사', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '검제', 'class': '귀검사', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '디어사이드', 'class': '귀검사', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '마제스티', 'class': '귀검사', 'gender': 'F', 'type': 'D'})
#
# db.jobs.insert_one({'job': '패황', 'class': '격투가', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '명왕', 'class': '격투가', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '그랜드%20마스터', 'class': '격투가', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '염황%20광풍제월', 'class': '격투가', 'gender': 'M', 'type': 'D'})
#
# db.jobs.insert_one({'job': '염제%20폐월수화', 'class': '격투가', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '카이저', 'class': '격투가', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '용독문주', 'class': '격투가', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '얼티밋%20디바', 'class': '격투가', 'gender': 'F', 'type': 'S'})
#
# db.jobs.insert_one({'job': '커맨더', 'class': '거너', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '프라임', 'class': '거너', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '디스트로이어', 'class': '거너', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '레이븐', 'class': '거너', 'gender': 'M', 'type': 'D'})
#
# db.jobs.insert_one({'job': '크림슨로제', 'class': '거너', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '스톰트루퍼', 'class': '거너', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '프레이야', 'class': '거너', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '옵티머스', 'class': '거너', 'gender': 'F', 'type': 'D'})
#
# db.jobs.insert_one({'job': '어센션', 'class': '마법사', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '아이올로스', 'class': '마법사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '뱀파이어%20로드', 'class': '마법사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '오블리비언', 'class': '마법사', 'gender': 'M', 'type': 'D'})
#
# db.jobs.insert_one({'job': '지니위즈', 'class': '마법사', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '아슈타르테', 'class': '마법사', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '오버마인드', 'class': '마법사', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '이클립스', 'class': '마법사', 'gender': 'F', 'type': 'S'})
#
# db.jobs.insert_one({'job': '태을선인', 'class': '프리스트', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '이모탈', 'class': '프리스트', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '저스티스', 'class': '프리스트', 'gender': 'M', 'type': 'D'})
#
# db.jobs.insert_one({'job': '인페르노', 'class': '프리스트', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '천선낭랑', 'class': '프리스트', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '리디머', 'class': '프리스트', 'gender': 'F', 'type': 'D'})
#
# db.jobs.insert_one({'job': '세이비어', 'class': '나이트', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '드레드노트', 'class': '나이트', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '가이아', 'class': '나이트', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '마신', 'class': '나이트', 'gender': 'F', 'type': 'D'})
#
# db.jobs.insert_one({'job': '제노사이더', 'class': '마창사', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '에레보스', 'class': '마창사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '듀란달', 'class': '마창사', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '워로드', 'class': '마창사', 'gender': 'M', 'type': 'D'})
#
# db.jobs.insert_one({'job': '언터처블', 'class': '총검사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '갓파더', 'class': '총검사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '패스파인더', 'class': '총검사', 'gender': 'M', 'type': 'S'})
# db.jobs.insert_one({'job': '레퀴엠', 'class': '총검사', 'gender': 'M', 'type': 'D'})
#
# db.jobs.insert_one({'job': '다크나이트', 'class': '다크나이트', 'gender': 'M', 'type': 'D'})
# db.jobs.insert_one({'job': '크리에이터', 'class': '크리에이터', 'gender': 'F', 'type': 'S'})
#
# db.jobs.insert_one({'job': '그림리퍼', 'class': '도적', 'gender': 'F', 'type': 'S'})
# db.jobs.insert_one({'job': '시라누이', 'class': '도적', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '타나토스', 'class': '도적', 'gender': 'F', 'type': 'D'})
# db.jobs.insert_one({'job': '알키오네', 'class': '도적', 'gender': 'F', 'type': 'D'})

job = list(db.jobs.find({}, { "_id": 0}))

#랭킹 1~4페이지까지 링크 크롤링
urls = []
types = []
for i in range (0, len(job)):
    for j in range(1, 2):
        base_url_1 = 'https://dunfaoff.com/ranking.df?jobName='
        base_url_2 = '&jobGrowName='
        base_url_3 = '&gender='
        base_url_4 = '&page='
        url = base_url_1 + job[i]['class'] + base_url_2 + job[i]['job'] + base_url_3 + job[i]['gender'] + base_url_4 + str(j)
        urls.append(url)
        types.append(job[i]['type'])


# print(types)
# print(urls)
# print(len(urls))
#div_rank > b:nth-child(3)


#랭킹 1~4페이지까지 각각 캐릭 정보 페이지 링크 크롤링
db.rank.delete_many({})
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
        # db.rank.update(char_db, char_db, upsert=True)


mythic = list(db.rank.find({}, { "_id": 0}))
new_urls = []
for i in range(0, len(mythic)):
    url1 = 'https://dunfaoff.com/SearchResult.df?server='
    url2 = '&characterid='
    url_api = url1 + mythic[i]['server_id'] + url2 + mythic[i]['char_id']
    new_urls.append(url_api)
print(new_urls)


mythics = ['가네샤의 영원한 가호', '결속의 체인 플레이트', '고대 심연의 로브', '군신의 마지막 갈망', '길 방랑자의 물소 코트',
           '낭만적인 선율의 왈츠', '대 마법사 [???]의 로브', '대제사장의 예복', '또다른 시간의 흐름', '라이도 : 질서의 창조자',
           '사탄 : 분노의 군주', '새벽을 녹이는 따스함', '생사를 다스리는 그림자의 재킷', '선택이익', '세상을 삼키는 분노', '수석 집행관의 코트',
           '숙명을 뒤엎는 광란', '시간을 거스르는 자침', '아린 고통의 비극', '영명한 세상의 순환', '영원을 새긴 바다', '영원한 나락의 다크버스',
           '영원히 끝나지 않는 탐구', '운명을 거스르는 자', '원시 태동의 대지', '웨어러블 아크 팩', '작열하는 대지의 용맹',
           '종말의 역전', '지고의 화염 - 이프리트', '차원을 관통하는 초신성', '천상의 날개', '천지에 울려퍼지는 포효', '최후의 전술', '트로피카 : 드레이크', '플라즈마 초 진공관',]

count = []
for i in range (0, len(mythic)):
    count.append(0)

#item-list > table > tbody > tr:nth-child(11) > td > div:nth-child(2) > div > a.tvitemName
#item-list > table > tbody > tr:nth-child(1) > td > div:nth-child(2) > div > a.tvitemName
#item-list > table > tbody > tr:nth-child(4) > td > div:nth-child(2) > div:nth-child(1) > a.tvitemName

for i in range(0, len(new_urls)):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(new_urls[i], headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    equipment = soup.select('#item-list > table > tbody > tr:nth-child(3) > td > div:nth-child(2) > div > a.tvitemName')
    print(equipment)





# #랭킹 1~5페이지까지 각각 캐릭 정보 페이지 링크 크롤링
# characterid = []
# serverid = []
# points = []
# names = []
# for i in range(0, len(urls)):
#     headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(urls[i], headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     # div_rank > b:nth-child(3)
#     # div_damage > b:nth-child(1)
#     char_info = soup.select('#back > div > div.col-sm-12.col-md-12.col-xl-8.col-lg-8 > div > div:nth-child(4) > div')
#     for info in char_info:
#         server_id = info['server']
#         char_id = info['characterid']
#         point = info.select_one('#div_damage > b:nth-child(1)')
#         name = info.select_one('#div_rank > b:nth-child(3)')
#         characterid.append(char_id)
#         serverid.append(server_id)
#         points.append(point.text)
#         names.append(name.text)
#     print('진행중: ' + str(i) + '/' + str(len(urls)))
# print('완료')
# print(characterid)
# print(serverid)
# print(points)
# print(names)


# #랭킹 1~5페이지까지 전 직업 캐릭터명 저장
# # db.rank.delete_many({})
# for i in range(0, len(rank_url)):
#     data = requests.get(rank_url[i], headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#
#     name = soup.select_one('#char_name').text
#     server = soup.select_one('#char_server').text
#     job = soup.select_one('#char_info').text
#     damage = soup.select_one('#skill_damage > div:nth-child(5) > div.dmgRow > b.sinergeDmg0').text
#
#     char = {
#         'name': name,
#         'server': server,
#         'job': job[30:],
#         'damage': damage,
#         'url': rank_url[i]
#     }
#     db.rank.insert_one(char)
#     db.rank.update(char, char, upsert=True)
#     print('완료!' + str(i) + '/' + str(len(rank_url)))
#
# driver.close()