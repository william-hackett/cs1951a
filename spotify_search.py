from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import json

with open('spotify_auth.json') as json_file:
    data = json.load(json_file)

CONSUMER_KEY = data["CONSUMER-KEY"]
CONSUMER_SECRET = data["CONSUMER-SECRET"]


client_credentials_manager = SpotifyClientCredentials(client_id=CONSUMER_KEY, client_secret=CONSUMER_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    tid = 'spotify:track:4TTV7EcfroSLWzXRY6gLv6'

start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start
print(json.dumps(analysis, indent=4))
print ("analysis retrieved in %.2f seconds" % (delta,))
