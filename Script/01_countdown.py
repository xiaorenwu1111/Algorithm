# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:18:48 2018

@author: lenovo
"""

def countdown(i):
  print(i)
  # base case
  if i <= 0:
    return
  # recursive case
  else:
    countdown(i-1)

countdown(5)