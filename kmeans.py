#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 00:04:27 2019

@author: sarahcstuart
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import numpy.random
import csv
import matplotlib.pyplot as plt
import random
import seaborn as sns
import collections
from collections import Counter



# READ IN DATA
f = open("SpotifyFeatures.csv", "rt", encoding="utf8")
csvReader  = csv.DictReader(f)


acGenres = []
X = []

for cLine in csvReader:
    if random.random() < .01:
        acGenres.append(cLine["artist_name"])
        X.append( ( float(cLine["acousticness"]), float(cLine["danceability"])  
		#float(cLine["energy"]),float(cLine["instrumentalness"]),float(cLine["liveness"]),
        #float(cLine["loudness"]),float(cLine["speechiness"]),float(cLine["valence"])   
		 ) )


acGenres = np.array(acGenres)
X           = np.array(X)


N = len(X)



#At this point data is loaded.

def distance(A, B):
	return np.sum( (A-B)**2 )


# K MEANS CLUSTERING
K = 10

counter = 50
old_within_cluster_spr = np.inf

#def k_means(K):
while (counter > 0):

# set initial clusters
	aXmeans_byCluster = np.random.rand( K, X.shape[1]) * (np.max(X, axis=0) - np.min(X, axis=0)) + np.min(X, axis=0)
	aiCluster = np.zeros(N, int)

	
	old_means = []
#print (distance ( X[1], X[2]))
#i feel like distance should compute for more than one dimension
	old_means = np.zeros((K, len(X[0])))


	while distance(aXmeans_byCluster, old_means) > 0:

# TODO: Loop the following until convergence
		klist= []
		withinClustSpread = 0 


		for i in range(N):
    # TODO: Allocate each country to nearest cluster
			minDist = np.inf


			for k in range(K):
				if distance(aXmeans_byCluster[k], X[i]) < minDist:
					minDist = distance(aXmeans_byCluster[k], X[i])
					#print(minDist, i, k) 
					aiCluster[i]=k 

			withinClustSpread = withinClustSpread + (distance(X[i], aXmeans_byCluster[aiCluster[i]]))
	# for i in range(N):
			for kk in range(K):
				klist = X[aiCluster == kk]
				old_means = aXmeans_byCluster
				aXmeans_byCluster[k] = np.apply_along_axis(np.mean, axis = 0, arr = klist)
				#print(aXmeans_byCluster)


	
	counter = counter - 1

	if old_within_cluster_spr > withinClustSpread:
		old_within_cluster_spr = withinClustSpread

print(aiCluster[0], "aicluster0")
print(aiCluster[0], "aicluster0") 

       
        
group0 = []
group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
group6 = []
group7 = []
group8 = []
group9 = []



        
for p in range(N):
    if aiCluster[p] == 0:
        group0.append(acGenres[p])
    elif aiCluster[p] == 1:
        group1.append(acGenres[p])
    elif aiCluster[p] == 2:
        group2.append(acGenres[p])
    elif aiCluster[p] == 3:
        group3.append(acGenres[p])
    elif aiCluster[p] == 4:
        group4.append(acGenres[p])
    elif aiCluster[p] == 5:
        group5.append(acGenres[p])
    elif aiCluster[p] == 6:
        group6.append(acGenres[p])
    elif aiCluster[p] == 7:
        group7.append(acGenres[p])
    elif aiCluster[p] == 8:
        group8.append(acGenres[p])
    elif aiCluster[p] == 9:
        group9.append(acGenres[p])
        

print(group0)
print(group1)
print(group2)
print(group3)
print(group4)
print(group5)
print(group6)
print(group7)
print(group8)
print(group9)


 
        
#plt.scatter(X[:, 0], X[:, 1], s=50);
#plt.scatter(aXmeans_byCluster[:, 0], X[:, 1], s=1);


plt.scatter(X[:, 0], X[:, 1],c=aiCluster, s=50, cmap='viridis');
plt.show
centers = aXmeans_byCluster
plt.scatter(centers[:, 0], centers[:, 1], s=200, alpha=0.5);
plt.show


plt
kmeans3 = 230
kmeans2 = 400
kmeans1 = 550
kmeans4 = 200
kmeans5 = 180
kmeans6 = 179
kmeans7 = 181
'''
def plot_corr(X,size=10):
    corr = X.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns);
    
    plot_corr(X)
    

corr = X.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
    
    

		#if aiCluster[i] == k:
			


#for j in range(N)
#		if aiCluster[j] == k:
#			klist.append(j)
#		meank = np.sum(X[j])/len(klist)	



#print(wCS)
#print(aiCluster)

'''