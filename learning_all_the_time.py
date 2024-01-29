#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:48:55 2024

@author: siobhanie
"""

# from terminal: python learning_all_the_time.py 
# Make sure that Conda environment is activated
# https://saturncloud.io/blog/troubleshooting-guide-when-your-conda-environment-doesnt-show-up-in-vs-code/


from numpy import *
import numpy as np

def newtons_method(x):
    
    for i in range(10):
        x = x - f(x)/fprim(x)
        
        
    return x


def f(x):
    return -sin(x)

def fprim(x):
    return -cos(x)


x0 = 3
zero1 = newtons_method(x0) 
print(zero1)