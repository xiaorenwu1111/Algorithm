# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:39:03 2018

@author: lenovo
"""
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <=pivot]
        greater = [i for i in array[1:] if i >= pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
    
print(quicksort([10, 5, 2, 3]))

