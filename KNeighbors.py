#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:20:28 2019

@author: sarahcstuart
"""
#from skimage import io
import numpy as np
import random
import numpy.matlib
import math
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

import numpy as np
import numpy.random
import csv
import matplotlib.pyplot as plt
import random
import seaborn as sns
from collections import Counter
from LyricsGetter import PyLyrics3 
import sys
sys.path.append("Words.py")
#from Words import *
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from numpy.random import rand


# READ IN DATA
f = open("SpotifyFeatures.csv", "rt", encoding="utf8")
csvReader  = csv.DictReader(f)
print(f)

lyrics = PyLyrics3()


#Set Y and X empty lists
Genres = []
Artist = []
Track = []
X = []
popularity = []

#READ IN DATA
for cLine in csvReader:
    if float(cLine["popularity"]) > 60 and (cLine["track_name"] not in Track):
     #if (random.random() < .001) and (cLine["track_name"] not in Track):
        try:
            song_lyrics = lyrics.get_song_lyrics(cLine["artist_name"].lower(), cLine["track_name"].lower())
            stop_words = set(stopwords.words('english'))
            myStop = []
            
        except TypeError: song_lyrics = False
        except IndexError: song_lyrics = False
        finally:
            if song_lyrics:
                popularity.append(cLine["popularity"])
                Genres.append(cLine["genre"])
                Artist.append(cLine["artist_name"])
                Track.append(cLine["track_name"])
                #for w in song_lyrics: 
                    #if w in stop_words: 
                        #myStop.append(w)
                love_count = 0
                baby_count = 0
                yeah_count = 0
                time_count = 0
                girl_count = 0
               # love_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("love"), song_lyrics))
              #  baby_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("baby"), song_lyrics))
               # yeah_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("yeah"), song_lyrics))
               # time_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("time"), song_lyrics))
               # girl_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("girl"), song_lyrics))
                
               # print(love_count, "love count")
                X.append( ( float(cLine["danceability"]),
        float(cLine["speechiness"]),
        float(cLine["instrumentalness"])
        ,float(cLine["liveness"]),
       float(cLine["loudness"]),float(cLine["speechiness"]),float(cLine["valence"])   
         ) )


Genres = np.array(Genres)
Track = np.array(Track)
Artist = np.array(Artist)
X           = np.array(X)

#USE API TO GET ALL THE DATA

Neighbs = NearestNeighbors()


def getNeighbors(songIndex, n):
    Neighbs.fit(X)
    mySongData = X[songIndex]
    mySong = Track[songIndex]
    myArtist = Artist[songIndex]
    coords, TestNeighbors = Neighbs.kneighbors(mySongData, n) 
    neighbors = []
    for i in TestNeighbors[0]:
        neighbors.append((Track[int(i)], Artist[int(i)]))
    print(mySong, myArtist, neighbors)
        
def get_recs(song): 
    my_song_index = numpy.where(Track==song)
    if len(my_song_index) < 1:
        print("NOT IN CORPUS (YET)")
    else:
        getNeighbors(my_song_index[0], 5)
        
get_recs("Moody Orange")
        
        
        
def make3dplot(): 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')    
    for i in range(len(X)): # plot each point + it's index as text above
      x = X[i][0]
      y = X[i][1]
      z = X[i][2]
      label = Artist[i]
      ax.scatter(x, y, z, color='r')
      ax.text(x, y, z, '%s' % (label), size=5, zorder=1, color='k')
    
    ax.set_xlabel('dancability')
    ax.set_ylabel('Speechiness')
    ax.set_zlabel('InstrumentalNess')
    
    for angle in range(0, 360, .1):
      ax.view_init(30, angle)
      plt.draw()
      plt.pause(.01)

