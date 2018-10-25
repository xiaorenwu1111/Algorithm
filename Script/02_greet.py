# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:19:36 2018

@author: lenovo
"""

def greet2(name):
    print("how are you, ", name, "?")

def bye():
    print("ok bye!")

def greet(name):
    print("hello, ", name, "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

greet("adit")