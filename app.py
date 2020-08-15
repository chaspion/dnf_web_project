from pymongo import MongoClient, DESCENDING

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/info', methods=['POST'])
# def post_orders():
#     server_r = request.form['server_give']
#     name_r = request.form['name_give']
#
#     info = {
#         'server': server_r,
#         'name': name_r
#     }
#
#     db.info.insert_one(info)
#     return jsonify({'result': 'success'})
#
# @app.route('/info', methods=['GET'])
# def get_orders():
#     basic_info = list(db.info.find({}, {'_id': 0}))
#     return jsonify({'result': 'success', 'basic_info': basic_info})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)