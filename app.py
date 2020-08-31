from pymongo import MongoClient, DESCENDING

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# client = MongoClient('mongodb://chaspion:tkfkdgo3@3.35.53.238', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/epic', methods=['GET'])
def show_items():
    epics = list(db.epics.find({}, {"_id": False}).sort('_id', DESCENDING))
    return jsonify({'result': 'success', 'epics': epics})

@app.route('/api/ranking', methods=['GET'])
def show_ranking():
    ranking = list(db.rank.find({}, {"_id": False}).sort('damage', DESCENDING))
    return jsonify({'result': 'success', 'ranking': ranking})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)