# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:45:22 2017
This code shows Kmeans algorithm using pandas when we have only two coordinates X,Y and two clusters
The purpose of this code is to not to show programming capability. it just shows how easy to develop 
machine learning algorithm in pandas comparing to numpy.
@author: Abdulrahman
"""
import pandas as pd

import numpy as np
no_points = 10
k= 2
no_iterations=200
#==============================================================================
# create a dataframe of rows representing the X,Y coordinates
# and then transform it in order to have X and Y coordinates in columns.
# since in panda is easier to work with columns than rows
#==============================================================================
data = pd.DataFrame ([np.random.randn(no_points), np.random.randn(no_points)] , index =['Xd', 'Yd'])
data = data.T

centers = pd.DataFrame([np.random.choice(data['Xd'],k) , np.random.choice(data['Yd'], k)], index = ['Xc', 'Yc'])
centers= centers.T


for i in range (no_iterations):
   
#==============================================================================
#substract all X coordinates from center, similarly with y.
#==============================================================================
        X_diff = pd.DataFrame([  pow((data['Xd'] - centers['Xc'][i] ),2)   for i in range (centers['Xc'].size)])
        Y_diff = pd.DataFrame ([ pow (( data['Yd'] - centers['Yc'][i]) ,2) for i in range (centers['Yc'].size)])

        X_diff= X_diff.T
        Y_diff = Y_diff.T


        X_diff.columns = [ 'd'+ str(i) for i in range (k)]
        Y_diff.columns = ['d1', 'd2']

        Sum = X_diff.add(Y_diff, fill_value =0)
#==============================================================================
# we apply euclidian distance and save the distances in distance dataframe
#==============================================================================
        distance =Sum.applymap(lambda x: np.sqrt(x))
#==============================================================================
# for each point, we select which cluster is the nearest
#==============================================================================
        clusters = distance.idxmin(axis =1)
#==============================================================================
# We got the index of each points belonging to each cluster        
#==============================================================================
        cluster1_index= clusters[clusters =='d1'].index
        cluster2_index= clusters [clusters== 'd2'].index
#==============================================================================
# we retrieve the x value and y value at the indices found in the previous step
#==============================================================================
        cluster1 = pd.concat([data['Xd'][cluster1_index] ,data['Yd'][cluster1_index] ]  , axis =1)
        cluster2= pd.concat([data['Xd'][cluster2_index] , data ['Yd'][cluster2_index]],axis =1)
#==============================================================================
# Updating the centers , concate it and transform it so the coordinates appear on columns
#==============================================================================
        centers1 = cluster1.mean(axis =0)
        centers2 = cluster2.mean(axis =0)
        centers =pd.concat([centers1, centers2], axis =1)
        centers= centers.T
        centers.columns = ['Xc', 'Yc']
  