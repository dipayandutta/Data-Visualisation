# -*- coding: utf-8 -*-

class Node(object):
    
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
        
    def set_data(self,data=None):
        self.data = data
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
        
    def set_next(self,new_next):
        self.next_node = new_next
        
    
class LinkedList:
    
    def __init__(self,head=None):
        self.head = head
        self.size = 0
        
    def get_size(self):
        return self.size
    
    def addNode(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size += 1
        return data
        
    def printNode(self):
        curr = self.head
        while curr:
            print curr.data
            curr = curr.get_next()
            
myList = LinkedList()
print "Inserting Data"
print myList.addNode(1)
print myList.addNode(3)
print myList.addNode(23)
print myList.addNode(21)

print "Printing Data ..."
print myList.printNode()

print "Size of the Linked List ..."
print myList.get_size()