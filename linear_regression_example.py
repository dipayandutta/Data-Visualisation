# -*- coding: utf-8 -*-

from math import sqrt

# Calculate the root mean square error

def rmse_error(actual,predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i]-actual[i]
        sum_error += (prediction_error**2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)
    
# Regression algorithm on the traning dataset

def eval_algo(dataset,algo):
    test_list = list()
    for row in dataset:
        row_copy = list(row)
        row_copy[-1] = None
        test_list.append(row_copy)
    predicted = algo(dataset,test_list)
    print predicted
    actual = [row[-1] for row in dataset]
    rmse = rmse_error(actual,predicted)
    return rmse

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values)/float(len(values))

# Calculate the co-variance between x and y
def covariance(x,mean_x,y,mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x)*(y[i]-mean_y)
    return covar

# Calculate the variance of a list of numbers
def variance(values,mean):
    return sum([(x-mean)**2 for x in values])
    
#  Calculate coefficients
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean , y_mean = mean(x),mean(y)
    b1= covariance(x,x_mean,y,y_mean) / variance(x,x_mean)
    b0 = y_mean - b1*x_mean
    return [b0,b1]

# Linear Regression Algorithm
def linear_regression(train,test):
    predictions = list()
    b0,b1 = coefficients(train)
    for row in test:
        yhat = b0 +b1*row[0]
        predictions.append(yhat)
    return predictions
    
# Test linear regression
dataset = [[1,1],[2,3],[4,5],[6,7]]
rmse = eval_algo(dataset,linear_regression)
print "RMSE %.3f"%(rmse)