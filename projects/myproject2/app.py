twitter_consumer_key = "o3OZXfhyhQpmQlMdbiyK6v5om"
twitter_consumer_secret = "Csc2uzueMWnCLJ5FOjcEpxVSf5S59RLdVfXrVn5vM6o1QyMTeZ"  
twitter_access_token = "921713602012184577-tgf3kbR0U2c07kYZJJj689Tiaxlq9iV"
twitter_access_secret = "InEDDJmoj0grYmwo3cGWZAMPHGd6HaUOyOnKk2VNiUZn1"

import twitter

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/poem', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    all_poems = list(db.poems.find({},{'_id':0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'poems':all_poems})

## API 역할을 하는 부분
@app.route('/poem', methods=['POST'])
def saving():
    
    # 1. 클라이언트로부터 데이터를 받기
    twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

    account = "@S2_feeling"

    poems = twitter_api.GetUserTimeline(screen_name=account, count=10, include_rts=True, exclude_replies=False)

	# 2. data를 스크래핑하기
    for poem in poems:
        
        resource_poem = poem.text
        
        body = resource_poem.split(': ',1)[0].rstrip()
        
        try:
             resource_poet = resource_poem.split(': ',1)[1]
             poet = resource_poet.split(', ',1)[0]
             book = resource_poet.split(', ',1)[1]
             print(body,poet,book)
        
        except:pass
            
        doc = {
                'body' : body,
                'poet' : poet,
                'book' : book
                }
        
        db.poems.insert_one(doc) # 3. mongoDB에 데이터 넣기

    return jsonify({'result': 'success', 'msg':'시를 읽어왔습니다'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)