import oauth2 as oauth
import json

with open('twitter_auth.json') as json_file:
    data = json.load(json_file)

CONSUMER_KEY = data["CONSUMER-KEY"]
CONSUMER_SECRET = data["CONSUMER-SECRET"]

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key=CONSUMER_KEY,
    secret=CONSUMER_SECRET)

# Request token URL for Twitter.
# Trends for global, WOEID = 1 is global
request_token_url = "https://api.twitter.com/1.1/trends/place.json?id=1"

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")
print resp
print content
