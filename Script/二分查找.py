# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:06:20 2018

@author: liyufang
"""
def binary_search(list,item):
    low=0
    high = len(list)-1
    
    while low <= high :
        mid = (low + high)/2
        guess = list[mid]
        if guess == item :
            return mid
        if guess > item :
            high = mid -1
        else:
            low = mid + 1
        return None
    
mylist = [1,3,5,7,9]
print(binary_search(mylist,3)) # =>1
            
