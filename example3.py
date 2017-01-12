# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:30:42 2017

@author: groot
"""


import sys
import numpy as np

filename = open('sonar-data.csv')

xList = []
labels= []

for line in filename:
    row = line.strip().split(",")
    xList.append(row)
    
col = 3
colData = []
ncol = len(xList)

counter = 0
for row in xList:
    counter += 1
    if counter == ncol:
        sys.exit
    else:
        colData.append(float(row[col]))
        
        
print len(colData)
'''
for row in colData:
    print row
'''     
colArray = np.array(colData) #Converting Data into array
colMean = np.mean(colArray)
colsd    = np.std(colArray)

print colMean
print colsd


#Calculare quantile boundaries
ntiles = 4
percentBdry = []

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray,i*(100)/ntiles))
print percentBdry