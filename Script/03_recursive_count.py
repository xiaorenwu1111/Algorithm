# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:32:55 2018

@author: lenovo
"""
def count(list):
    if list == []:
        return 0
    return 1+count(list[1:])




