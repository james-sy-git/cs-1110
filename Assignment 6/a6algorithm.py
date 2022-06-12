"""
Primary algorithm for k-Means clustering

This file contains the Algorithm class for performing k-means clustering.  While it is
the last part of the assignment, it is the heart of the clustering algorithm.  You
need this class to view the complete visualizer.

James Sy (jcs547)
11/17/21
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6dataset
import a6cluster

# Part A
def valid_seeds(value, size):
    """
    Returns True if value is a valid list of seeds for clustering.

    A list of seeds is a k-element list OR tuple of integersa between 0 and size-1.
    In addition, no seed element can appear twice.

    Parameter valud: a value to check
    Precondition: value can be anything

    Paramater size: The database size
    Precondition: size is an int > 0
    """
    assert type(size) == int and size > 0, 'size not an int greater than zero'
    if type(value) != list and type(value) != tuple:
        return False
    ret_val = True
    for x in value:
        if type(x) != int:
            ret_val = False
        elif x < 0 or x > (size-1):
            ret_val = False
        elif value.count(x) != 1:
            ret_val = False

    return ret_val


class Algorithm(object):
    """
    A class to manage and run the k-means algorithm.

    The method step() performs one step of the calculation.  The method run() will
    continue the calculation until it converges (or reaches a maximum number of steps).
    """
    # IMMUTABLE ATTRIBUTES (Fixed after initialization with no DIRECT access)
    # Attribute _dataset: The Dataset for this algorithm
    # Invariant: _dataset is an instance of Dataset
    #
    # Attribute _cluster: The clusters to use at each step
    # Invariant: _cluster is a non-empty list of Cluster instances

    # Part B
    def getClusters(self):
        """
        Returns the list of clusters in this object.

        This method returns the cluster list directly (it does not copy).  Any changes
        made to this list will modify the set of clusters.
        """
        return self._cluster


    def __init__(self, dset, k, seeds=None):
        """
        Initializes the algorithm for the dataset ds, using k clusters.

        If the optional argument seeds is supplied, those seeds will be a list OR
        tuple of indices into the dataset. They specify which points should be the
        initial cluster centroids. Otherwise, the clusters are initialized by randomly
        selecting k different points from the database to be the cluster centroids.

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter k: the number of clusters
        Precondition: k is an int, 0 < k <= dset.getSize()

        Paramter seeds: the initial cluster indices (OPTIONAL)
        Precondition: seeds is None, or a list/tuple of valid seeds.
        """
        assert isinstance(dset, a6dataset.Dataset), 'dset not Dataset instance'
        self._dataset = dset

        assert type(k) == int, 'k is not an int'
        assert (0 < k <= dset.getSize()) == True, 'k out of valid cluster range'
        list = []
        size = self._dataset.getSize()

        if seeds != None:
            assert valid_seeds(seeds, size) == True, 'seeds are not valid'
            for x in range(k):
                seeded = a6cluster.Cluster(dset, dset.getContents()[seeds[x]])
                list.append(seeded)

        elif seeds == None:
            rand_clusters = random.sample(dset.getContents(), k)
            for y in range(k):
                seedless = a6cluster.Cluster(dset, rand_clusters[y])
                list.append(seedless)

        self._cluster = list


    # Part C
    def _nearest(self, point):
        """
        Returns the cluster nearest to point

        This method uses the distance method of each Cluster to compute the distance
        between point and the cluster centroid. It returns the Cluster that is closest.

        Ties are broken in favor of clusters occurring earlier in the list returned
        by getClusters().

        Parameter point: The point to compare.
        Precondition: point is a tuple of numbers (int or float). Its length is the
        same as the dataset dimension.
        """
        assert a6dataset.is_point(point), 'point is not a valid point'
        assert len(point) == self._dataset.getDimension(), 'incorrect point dimension'

        near_distance = (self._cluster[0]).distance(point)
        near_cluster = self._cluster[0]

        for x in range(len(self._cluster)):
            if (self._cluster[x]).distance(point) < near_distance:
                near_cluster = self._cluster[x]
                near_distance = (self._cluster[x]).distance(point)

        return near_cluster


    def _partition(self):
        """
        Repartitions the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.
        for x in self._cluster:
            x.clear()
        for y in range(len(self._dataset.getContents())):
            datapoint = self._dataset.getContents()[y]
            near_cluster = self._nearest(datapoint)
            near_cluster.addIndex(y)


    # Part D
    def _update(self):
        """
        Returns True if all centroids are unchanged after an update; False otherwise.

        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It returns False if just one has
        changed. Otherwise, it returns True.
        """
        checklist = []
        ret_val = True
        for x in self._cluster:
            checklist.append(x.update())
        for y in checklist:
            if y == False:
                ret_val = False

        return ret_val


    def step(self):
        """
        Returns True if the algorithm converges after one step; False otherwise.

        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns the appropriate result (True if
        converged, false otherwise).
        """
        # In a cycle, we partition the points and then update the means.
        self._partition()
        if self._update() == True:
            return True
        elif self._update() == False:
            return False


    # Part D
    def run(self, maxstep):
        """
        Continues clustering until either it converges or performs maxstep steps.

        After the maxstep call to step, if this calculation did not converge, this
        method will stop.

        Parameter maxstep: The maximum number of steps to perform
        Precondition: maxstep is an int >= 0
        """
        # Call k_means_step repeatedly, up to maxstep times, until the algorithm
        # converges.  Stop once you reach maxstep iterations even if the algorithm
        # has not converged.
        # You do not need a while loop for this.  Just write a for-loop, and exit
        # the for-loop (with a return) if you finish early.
        assert type(maxstep) == int and maxstep >= 0, 'maxstep is not an int >= 0'
        steps = 0
        for x in range(maxstep):
            if self.step() == True:
                return
            elif self.step() == False:
                steps = steps + 1
                if steps == maxstep:
                    return
