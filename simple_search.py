# -*- coding: utf-8 -*-

number_list = [12,3,4,1.0,5,6]

search_item = 11
not_present = 0 

def found(number,number_list):
    print "Search Item found in position %d and item is %d"%(number,number_list[number])
    
def not_found(not_present,number_list):
    if not_present == len(number_list):
        print "Key not Found in the list"
        
        
for number in xrange(len(number_list)):
    if number_list[number] == search_item:
        found(number,number_list)
    else:
        not_present += 1
        not_found(not_present,number_list)
        

