# -*- coding: utf-8 -*-

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values) / float(len(values))
    
# Calculate the variance of a list of numbers

def variance(values,mean):
    return sum([(x-mean)**2 for x in values])
    
# dataset 
dataset = [[1,1],[2,3],[4,5],[6,7]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]

mean_x , mean_y = mean(x) , mean(y)
var_x , var_y   = variance(x,mean_x), variance(y,mean_y)

print x 
print y 
print mean_x 
print mean_y
print var_x
print var_y