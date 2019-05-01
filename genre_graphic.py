import json
import matplotlib.pyplot as plt
import numpy as np
import pprint

def main():
    with open('./genre_kmeans_out_percents.json') as results:
        cluster_list = json.load(results)

    
    pprint.pprint(cluster_list)

    genre_list = ['Alternative', \
                  'Blues', \
                  'Classical', 'Country', \
                  'Hip-Hop', 'Indie', \
                  'Pop', \
                  'Reggae', 'Rock', \
                  'Soul']
    clusters = 10
    #outer index: genre. Inner index: cluster
    #so when we're making the plot, we iterate through each list and add parts to everything for that
    genre_percents = [[0 for j in range(clusters)] for i in range(clusters)]
    ind = np.arange(clusters)

    for genre_i in range(len(genre_list)):
        for cluster_i in range(len(cluster_list)):
            if genre_list[genre_i] in cluster_list[cluster_i]:
                genre_percents[genre_i][cluster_i] = cluster_list[cluster_i][genre_list[genre_i]]
            #else:
             #   genre_percents[genre_i][cluster_i] = 0

        

    pprint.pprint(genre_percents)

    bar_list = []
    for i in range(clusters):
        bar_list.append(plt.bar(ind, genre_percents[i]))

    plt.legend([bar_list[i][0] for i in range(clusters)], genre_list)


    plt.savefig('genre_plot.png')




        



    """
    i = 0


    for i_cluster in range(len(cluster_list)):
        filename = 'cluster_graph_' + str(i) + '.png'
        i += 1

        cluster = cluster_list[i_cluster]
        genres = cluster.keys()
        y_pos = np.arange(len(genres))
        percent = [cluster[genre] * 100 for genre in genres]

        plt.bar(y_pos, percent, align = 'center', alpha=0.5)
        plt.xticks(y_pos, genres)
        plt.ylabel('Percent')
        plt.title('Percent of Genre Per Cluster')

        plt.savefig(filename)
    """

if __name__ == '__main__':
    main()
