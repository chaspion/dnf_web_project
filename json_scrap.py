import urllib.request, json
from pymongo import MongoClient, DESCENDING


# client = MongoClient('mongodb://chaspion:tkfkdgo3@13.125.243.111', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

db.mythic.update_many({}, {'$set': {'count': 0}})
ranking = list(db.rank.find({}, {"_id": False}).sort('rank_point', DESCENDING))
print(len(ranking))
for i in range (0, 200):
    char_url = 'https://api.neople.co.kr/df/servers/' + ranking[i]['server_id'] + '/characters/' + ranking[i]['char_id'] + '/equip/equipment?apikey=u24sm4DgTGNKceFknyhar93DXxuHX9pN'
    with urllib.request.urlopen(char_url) as url:
        data = json.loads(url.read().decode())
        for i in range(0, len(data['equipment'])):
            if data['equipment'][i]['itemRarity'] == '신화':
                name = data['equipment'][i]['itemName']
                item = db.mythic.find_one({'name': name})
                new_count = item['count'] + 1
                db.mythic.update_one({'name': name}, {'$set': {'count': new_count}})