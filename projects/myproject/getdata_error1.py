twitter_consumer_key = "o3OZXfhyhQpmQlMdbiyK6v5om"
twitter_consumer_secret = "Csc2uzueMWnCLJ5FOjcEpxVSf5S59RLdVfXrVn5vM6o1QyMTeZ"  
twitter_access_token = "921713602012184577-tgf3kbR0U2c07kYZJJj689Tiaxlq9iV"
twitter_access_secret = "InEDDJmoj0grYmwo3cGWZAMPHGd6HaUOyOnKk2VNiUZn1"

import twitter

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

account = "@S2_Feeling"
account2 = "@gain_sesang"

poems1 = twitter_api.GetUserTimeline(screen_name=account, count=5, include_rts=True, exclude_replies=False)
poems2 = twitter_api.GetUserTimeline(screen_name=account2, count=5, include_rts=True, exclude_replies=False)

poems = poems1 + poems2

for poem in poems1:

    resource_poem1 = poem.text

    body1 = resource_poem1.split(': ',1)
    body1_1 = body1[0].rstrip()


for poem in poems2:

    resource_poem2 = poem.text

    body2 = resource_poem2.split('| ',1)
    body2_1 = body2[0].rstrip()


body = body1_1 + body2_1

print(body)

