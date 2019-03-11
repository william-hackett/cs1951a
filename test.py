import oauth2 as oauth
import json

with open('data.json') as json_file:
    data = json.load(json_file)


for x in data:
    print(x["tweet_volume"])
