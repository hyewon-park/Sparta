from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def stars_list():
    stars = list(db.mystar.find({},{'_id':False}).sort('like',-1))
    return jsonify({'result': 'success','all_star':stars})


@app.route('/api/like', methods=['POST'])
def star_like():
    name_receive = request.form['name_give']

    like = db.mystar.find_one({'name': name_receive},{'_id':0})['like']
    new_like = like +1

    db.mystar.update_one({'name':name_receive},{'$set':{'like':new_like}})
    
    return jsonify({'result': 'success','msg':'완료되었습니다!'})


@app.route('/api/delete', methods=['POST'])
def star_delete():
    name_receive = request.form['name_give']

    db.mystar.delete_one({'name':name_receive})
    
    return jsonify({'result': 'success','msg':'삭제가 완료되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)