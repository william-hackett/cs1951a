import csv
import json
import numpy as np
from sklearn.cluster import KMeans

def gather_data(data_file):
    csv_reader = csv.DictReader(data_file, delimiter = ',')
    id_to_genre = {}
    index_to_id = []
    data = []
    i = 0
    for row in csv_reader:
        #If it's not a new song, we already have it in data, so we just add the new genre to our list of genres
        # for that song
        if row['track_id'] in id_to_genre:
            id_to_genre[row['track_id']].append(row['\ufeffgenre'])
        #otherwise, we add the id-genre_set pair, the metrics to our data, and the id to our list of id's 
        else:
            id_to_genre[row['track_id']] = [row['\ufeffgenre']]

            new_row = []
            new_row.append(row['acousticness'])
            new_row.append(row['danceability'])
            new_row.append(row['energy'])
            new_row.append(row['instrumentalness'])
            new_row.append(row['liveness'])
            new_row.append(row['loudness'])
            new_row.append(row['speechiness'])
            new_row.append(row['valence'])
            data.append(np.array(new_row))

            index_to_id.append(row['track_id'])
            i += 0


    #The gist of this strategy is that at the end, we will be able to use our labels
    # to get id's, and id's to get a set of genres for that point.
    data = np.array(data)
    
    return id_to_genre, index_to_id, data



    
def main():
    #get the data
    print('Reading data...')
    with open('./SpotifyFeats.csv') as song_file:
        genres, ids, data = gather_data(song_file)

    #set cluster_count here
    cluster_count = 26
    print('26 clusters')

    #run kmeans
    print('Running KMeans...')
    kmeans = KMeans(n_clusters = cluster_count).fit(data)
    labels = kmeans.labels_
    with open('./labels.json', 'w') as out_file:
        json.dump(labels.tolist(), out_file)

    genre_count = [{} for i in range(cluster_count)]
    total_count = [0 for i in range(cluster_count)]

    print('Sorting results...')
    for i in range(len(labels)):
        cluster = labels[i]
        song_id = ids[i]
        genre_list = genres[song_id]

        total_count[cluster] += 1

        for genre in genre_list:
            if genre in genre_count[cluster]:
                genre_count[cluster][genre] += 1
            else:
                genre_count[cluster][genre] = 1

    for i in range(len(genre_count)):
        for key, value in genre_count[i].items():
            genre_count[i][key] = value / total_count[i]

    with open('./genre_kmeans_out.json', 'w') as out_file:
        json.dump(genre_count, out_file)

if __name__ == '__main__':
    main()
