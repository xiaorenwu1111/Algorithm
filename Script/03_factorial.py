# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:20:45 2018

@author: lenovo
"""

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))