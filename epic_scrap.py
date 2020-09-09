import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

def character_scrap():
    client = MongoClient('mongodb://chaspion:tkfkdgo3@3.35.18.118', 27017)
    # client = MongoClient('localhost', 27017)
    db = client.dbsparta

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    data = requests.get("https://dunfaoff.com/ranking.df", headers = headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    db.jobs.delete_many({})
    db.jobs.insert_one({'job': '검신', 'class': '귀검사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '다크로드', 'class': '귀검사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '블러드%20이블', 'class': '귀검사', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '인다라천', 'class': '귀검사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '악귀나찰', 'class': '귀검사', 'gender': 'M', 'type': 'D'})

    db.jobs.insert_one({'job': '네메시스', 'class': '귀검사', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '검제', 'class': '귀검사', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '디어사이드', 'class': '귀검사', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '마제스티', 'class': '귀검사', 'gender': 'F', 'type': 'D'})

    db.jobs.insert_one({'job': '패황', 'class': '격투가', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '명왕', 'class': '격투가', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '그랜드%20마스터', 'class': '격투가', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '염황%20광풍제월', 'class': '격투가', 'gender': 'M', 'type': 'D'})

    db.jobs.insert_one({'job': '염제%20폐월수화', 'class': '격투가', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '카이저', 'class': '격투가', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '용독문주', 'class': '격투가', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '얼티밋%20디바', 'class': '격투가', 'gender': 'F', 'type': 'S'})

    db.jobs.insert_one({'job': '커맨더', 'class': '거너', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '프라임', 'class': '거너', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '디스트로이어', 'class': '거너', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '레이븐', 'class': '거너', 'gender': 'M', 'type': 'D'})

    db.jobs.insert_one({'job': '크림슨로제', 'class': '거너', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '스톰트루퍼', 'class': '거너', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '프레이야', 'class': '거너', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '옵티머스', 'class': '거너', 'gender': 'F', 'type': 'D'})

    db.jobs.insert_one({'job': '어센션', 'class': '마법사', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '아이올로스', 'class': '마법사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '뱀파이어%20로드', 'class': '마법사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '오블리비언', 'class': '마법사', 'gender': 'M', 'type': 'D'})

    db.jobs.insert_one({'job': '지니위즈', 'class': '마법사', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '아슈타르테', 'class': '마법사', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '오버마인드', 'class': '마법사', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '이클립스', 'class': '마법사', 'gender': 'F', 'type': 'S'})

    db.jobs.insert_one({'job': '태을선인', 'class': '프리스트', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '이모탈', 'class': '프리스트', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '저스티스', 'class': '프리스트', 'gender': 'M', 'type': 'D'})

    db.jobs.insert_one({'job': '인페르노', 'class': '프리스트', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '천선낭랑', 'class': '프리스트', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '리디머', 'class': '프리스트', 'gender': 'F', 'type': 'D'})

    db.jobs.insert_one({'job': '세이비어', 'class': '나이트', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '드레드노트', 'class': '나이트', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '가이아', 'class': '나이트', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '마신', 'class': '나이트', 'gender': 'F', 'type': 'D'})

    db.jobs.insert_one({'job': '제노사이더', 'class': '마창사', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '에레보스', 'class': '마창사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '듀란달', 'class': '마창사', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '워로드', 'class': '마창사', 'gender': 'M', 'type': 'D'})

    db.jobs.insert_one({'job': '언터처블', 'class': '총검사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '갓파더', 'class': '총검사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '패스파인더', 'class': '총검사', 'gender': 'M', 'type': 'S'})
    db.jobs.insert_one({'job': '레퀴엠', 'class': '총검사', 'gender': 'M', 'type': 'D'})

    db.jobs.insert_one({'job': '다크나이트', 'class': '다크나이트', 'gender': 'M', 'type': 'D'})
    db.jobs.insert_one({'job': '크리에이터', 'class': '크리에이터', 'gender': 'F', 'type': 'S'})

    db.jobs.insert_one({'job': '그림리퍼', 'class': '도적', 'gender': 'F', 'type': 'S'})
    db.jobs.insert_one({'job': '시라누이', 'class': '도적', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '타나토스', 'class': '도적', 'gender': 'F', 'type': 'D'})
    db.jobs.insert_one({'job': '알키오네', 'class': '도적', 'gender': 'F', 'type': 'D'})

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
            type = types[i]
            char_url = 'https://dunfaoff.com/SearchResult.df?server=' + info['server'] + '&characterid=' + info['characterid']

            if (('레이븐' in urls[i]) or ('디스트로이어' in urls[i]) or ('커맨더' in urls[i]) or ('프라임' in urls[i])):
                job = urls[i][55:-16].replace('%20', ' ')
            elif (('태을선인' in urls[i]) or ('이모탈' in urls[i]) or ('저스티스' in urls[i])) :
                job = urls[i][57:-16].replace('%20', ' ')
            else:
                job = urls[i][56:-16].replace('%20', ' ')


            print(server_id, char_id, point, name, job, type)

            char_db = {
                'char_id': char_id,
                'server_id': server_id,
                'rank_point': point,
                'char_name': name,
                'job': job,
                'type': type,
                'char_url': char_url
            }

            db.rank.insert_one(char_db)
            # db.rank.update(char_db, char_db, upsert=True)


if __name__ == "__main__":
    character_scrap()




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