# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:50:10 2018

@author: lenovo
"""

def findSmallest(arr):
    smallest = arr [0] #存储最小值
    smallest_index = 0 #存储最小值的索引
    for i in range(1,len(arr)):
        smallest = arr [i]
        smallest = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([5,3,6,2,10])
        
    
    