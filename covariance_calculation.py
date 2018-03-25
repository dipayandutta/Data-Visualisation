# -*- coding: utf-8 -*-

def mean(values):
    return sum(values) / float(len(values))
    
def covariance(x,mean_x , y,mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i]-mean_x)*(y[i]-mean_y)
    return covar
    
dataset = [[1,1],[2,3],[4,5],[6,7]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]

mean_x , mean_y = mean(x) , mean(y)
covar = covariance(x,mean_x,y,mean_y)

print mean_x
print mean_y
print covar
