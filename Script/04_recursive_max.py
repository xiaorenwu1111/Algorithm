# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:34:37 2018

@author: lenovo
"""
def max_(lst):
    if len(lst)==0:
        return None
    if len(lst)==1:
        return lst[0]
    else:
        sub_max =max_(lst[1:])
        return lst[0] if lst[0]> sub_max else sub_max




