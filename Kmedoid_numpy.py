# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:45:22 2017

@author: Abdulrahman
"""
import numpy as np

def dataInitialization(point_size, no_points, maxLimit, minLimit):
    x= np.zeros((no_points, point_size))
    for i  in range(point_size):
        x[:,i] = np.reshape ((maxLimit - minLimit) * np.random.random((no_points,1)) + (minLimit), no_points)
        return x
'''        
def centroidInitialization(x, no_clusters):
    c=[]
    for i in range (no_clusters):
        c.append([])
        
    for i in range (no_clusters):
        for j in range(x[0].size):
            a= np.random.random() * (np.max (x) - np.min(x)) + np.min(x)
            c[i].append(a)
    return c
'''
def clusterInitialization(no_clusters):
    clusters =[]
    for i in range (no_clusters):
        clusters.append([])
    return clusters

def eculidean_distance(c,x):
    sum = 0
    for i in range (len (x.T)):
        sum = sum + (pow((c[i] - x[i]),2))
    return np.sqrt(sum)
    
def euclidean_distance2(clusters, c):
    sum =0
    #centroid coordinates size equal to x Transpose size
    for i in range(len(clusters)):
        sum += (pow(c[i] - clusters[i],2))
   
    return np.sqrt(sum)
    
def findTotalCost(clusters,c):
    sum =0
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):

            sum += euclidean_distance2(clusters[i][j],c[i])
    cost = sum
    return cost
    
    
def swap (clusters, temp):
    print (temp)
    temp.append(clusters)
    print(temp)
    return temp
                

def distance (no_clusters):
    for  j in range (no_clusters):
        for i in range(len(x)):
            distance_matrix[j][i]= eculidean_distance(c[j], x[i])
            
        distanceT = distance_matrix.T
    return distanceT

def clustering(no_clusters,x):
    clusters[:]=[]
    
    for i in range (no_clusters):
        clusters.append([])
    print(clusters)
    print('clusters is intitialized')    
    
    distanceT = distance (no_clusters)
    
    for i in range (len(x)):
        print (i)
        k = np.argmin(distanceT[i])
        print (k)
        clusters[k].append(x[i])
        
    return
    
point_size =5
maxLimit =10
minLimit = 1
no_points = 20

x= np.array ([[ 2,6],[3,4],[3,8],[4,7],[6,2],[6,4],[7,3],[7,4],[8,5],[7,6]])

no_clusters =2
numberIterations =1
import random
c= random.sample(list (x),no_clusters)


clusters = clusterInitialization(no_clusters)
distance_matrix = np.zeros((no_clusters, len(x)))
totalcost = 0
print(c)

newCluster= True
noIteration = 0
while newCluster == True:
    noIteration = noIteration +1
    clustering(no_clusters, x)
    print(clusters)
    
    totalcost = findTotalCost(clusters, c)
    newCluster = False
    
    temp=[]
    
    for i in range (no_clusters):
        if newCluster == False:
            
            print ('i actually is' + repr(i))
            for j in range(len (clusters[i])):
                if newCluster == False:
                    
                    temp[:]=[]
                    temp= swap (clusters[i][j], temp)
                    for k in range(len(c)):
                        if k !=i:
                            temp.append(c[k])
                    print(temp)
                    findTotalCost(clusters, temp)
                    
                    if (findTotalCost(clusters, temp)) < totalcost:
                        totalcost = (findTotalCost(clusters, temp))
                        print('j is ' + repr(j))
                        print (totalcost)
                        print (" i is" + repr(c[i]))
                        print(temp[i])
                        print(i)
                        c[i] = temp[i]
                        print (c)
                        newCluster = True
                        print(' a new clustering procedure will start based on the new')
                        clustering(no_clusters,x)
                        print(clusters)
            print(totalcost)



    
