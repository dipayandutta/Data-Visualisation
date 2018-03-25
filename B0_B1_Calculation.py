# -*- coding: utf-8 -*-

# Calculate the mean of list of numbers
def mean(values):
    return sum(values) / float(len(values))
    
# Calculate the Covariance of a list of numbers
    
def covariance(x,mean_x,y,mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i]-mean_x)*(y[i]-mean_y)
    return covar
    
# Calculate the Variance of the list of numbers
    
def variance(values,mean):
    return sum([(x-mean)**2 for x in values])
    
# Calculate the co-efficient
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean,y_mean = mean(x),mean(y)
    b1 = covariance(x,x_mean,y,y_mean) / variance(x,x_mean)
    b0 = y_mean - b1*x_mean
    return [b0,b1]
    
# Dataset 
dataset = [[1,1],[2,3],[4,5],[6,7]]
b0,b1 = coefficients(dataset)
print "B0=%.3f,B1=%.3f"%(b0,b1)