import numpy as np
import matplotlib.pyplot as plt
import random

def make_random_points(number, min_height, max_height, min_weight, max_weight):
    """ make array of random height(x), and weight (y) tuples between bounds"""

    # make a list first then convert it to an array
    tmp = []
    for i in range(number):
        rand_height = random.uniform(min_height, max_height)
        rand_weight = random.uniform(min_weight, max_weight)
        tmp.append((rand_height, rand_weight))

    return np.array(tmp)

def cluster_content(data_points, centroids):
    """cluster submitted data points around submitted centroids -
       return as hash with cluster number referencing list of data points that
       are in that cluster """

    # make a hash to hold clusters and data points
    cluster = {}

    # for each data point, calculate the distance from each centroid and assign
    # data point to the cluster for the centroid that it has the minimum
    # distance from
    for x in data_points:

        # from sample code in class -- find centroid number that data point
        # x is the shortest distance from
        value = min([(i[0],np.linalg.norm(x - centroids[i[0]]))for i in enumerate(centroids)], key=lambda s:s[1])[0]

        # save x to list of data points for the cluster
        if value not in cluster:
            # initialize list for cluster if it doesn't exist yet
            cluster[value] = []

        cluster[value].append(x)

    return cluster

def matched(new_centroids, old_centroids):
    """function to determine if old_centroids and new_centroids contain the same data points"""
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))


def plot_cluster(centroids, cluster):
    """plot clustering solution, color each data point according to what cluster
       it's in and show '*'s for the k centroids"""

    # make array of built in color definitions to use for data points in
    # each cluster
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(centroids[:,0], centroids[:,1], marker = '*', s = 50, linewidths = 3, zorder = 10)
    plt.show()
    plt.title('new Cluster plot')

def new_center(cluster):
    """find new centers by finding the means for each cluster group"""
    keys = sorted(cluster.keys())
    new_centroids = np.array([(np.mean(cluster[k],axis = 0))for k in keys])

    return new_centroids



def do_k_means(data_points, k, n):
    """iteratively do kmeans until we can't improve chosen cluster centroids"""

    # randomly choose k centroids to start with

    # randomly get k integers and then use them as indexes in data points
    # to choose three random height,weight points to start calculations with
    temp_idxs = np.random.randint(n, size=k)
    old_centroids = np.array([data_points[i] for i in temp_idxs])

    # get three more centroids at random
    temp_idxs2 = np.random.randint(n, size=k)
    new_centroids = np.array([data_points[i] for i in temp_idxs2])

    # get initial clusters based on initial centroids
    cluster = cluster_content(data_points, old_centroids)
    iterations = 0

    # make a plot showing current centroids and where each data point is colored
    # according to what cluster it has been assigned to
    print(iterations, "iteration")
    plot_cluster(old_centroids, cluster)


    # keep choosing new centroids and clustering data points around them
    # until we get the same centroids as last time (meaning we can't improve)
    while not matched(new_centroids, old_centroids):
        iterations += 1
        old_centroids = new_centroids
        # cluster around new points and show another graph
        print(iterations, "iteration")
        cluster = cluster_content(data_points, new_centroids)
        plot_cluster(new_centroids, cluster)

        # find a new set of centroids
        new_centroids = new_center(cluster)

    # plot the last solution
    print(iterations, "iteration")
    plot_cluster(new_centroids, cluster)
    return

### main execution starts here ###


# ask user how many clusters we should make
num_clusters = int(input("How many clusters should we make? "))

# ask user how many test data points we should simulate
num_points = int(input("How many random test points should we make? "))

# ask user for upper and lower bounds of data points
min_height = int(input("Enter the minimum height (inches)? "))
max_height = int(input("Enter the maximum height (inches)? "))
min_weight = int(input("Enter the minimum weight (pounds)? "))
max_weight = int(input("Enter the maximum weight (pounds)? "))

# make random data points
random_data = make_random_points(num_points, min_height, max_height, min_weight, max_weight)

# make initial graph of random points
plt.scatter(random_data[:, 0], random_data[:, 1])
plt.show()
plt.title('Initial data scatter plot')

# loop and do kmeans clustering until we can't do any better
do_k_means(random_data, num_clusters, num_points)