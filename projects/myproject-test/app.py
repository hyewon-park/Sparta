twitter_consumer_key = "o3OZXfhyhQpmQlMdbiyK6v5om"
twitter_consumer_secret = "Csc2uzueMWnCLJ5FOjcEpxVSf5S59RLdVfXrVn5vM6o1QyMTeZ"  
twitter_access_token = "921713602012184577-tgf3kbR0U2c07kYZJJj689Tiaxlq9iV"
twitter_access_secret = "InEDDJmoj0grYmwo3cGWZAMPHGd6HaUOyOnKk2VNiUZn1"

import twitter

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

account = "@gain_sesang"

poems = twitter_api.GetUserTimeline(screen_name=account, count=10, include_rts=True, exclude_replies=False)


for poem in poems:

    resource_poem = poem.text
    body = resource_poem.split('| ',1)[0].rstrip()


    try:
        resource_poet = resource_poem.split('| ',1)[1]
        poet = resource_poet.split(', ',1)[0]

        book = resource_poet.split(', ',1)[1]
        print(body,poet,book)

    except:
        pass

    doc = {
        'body' : body,
        'poet' : poet,
        'book' : book
    }

    db.poems.insert_one(doc)