# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:45:22 2017

@author: Abdulrahman
"""
import pandas as pd

import numpy as np


no_points = 10
k= 2
no_iterations=200

data = pd.DataFrame ([np.random.randn(no_points), np.random.randn(no_points)] , index =['Xd', 'Yd'])


data = data.T

centers = pd.DataFrame([np.random.choice(data['Xd'],k) , np.random.choice(data['Yd'], k)], index = ['Xc', 'Yc'])

centers= centers.T

for i in range (no_iterations):
   
    
        X_diff = pd.DataFrame([  pow((data['Xd'] - centers['Xc'][i] ),2)   for i in range (centers['Xc'].size)])
        Y_diff = pd.DataFrame ([ pow (( data['Yd'] - centers['Yc'][i]) ,2) for i in range (centers['Yc'].size)])

        X_diff= X_diff.T
        Y_diff = Y_diff.T

        X_diff.columns = [ 'd'+ str(i) for i in range (k)]
       
        Y_diff.columns = ['d1', 'd2']

        Sum = X_diff.add(Y_diff, fill_value =0)

        distance =Sum.applymap(lambda x: np.sqrt(x))

        clusters = distance.idxmin(axis =1)
        
        cluster1_index= clusters[clusters =='d1'].index
        cluster2_index= clusters [clusters== 'd2'].index

        cluster1 = pd.concat([data['Xd'][cluster1_index] ,data['Yd'][cluster1_index] ]  , axis =1)

        cluster2= pd.concat([data['Xd'][cluster2_index] , data ['Yd'][cluster2_index]],axis =1)

#        data = data.drop(data.index ,axis =0)
#        data['Xd'] = cluster1['Xd']
#        data['Yd'] = cluster1 ['Yd']
        
        
    
        centers1 = cluster1.mean(axis =0)
        centers2 = cluster2.mean(axis =0)

        centers =pd.concat([centers1, centers2], axis =1)
        centers= centers.T
        centers.columns = ['Xc', 'Yc']
  