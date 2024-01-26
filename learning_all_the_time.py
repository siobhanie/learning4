#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:48:55 2024

@author: siobhanie
"""

from numpy import *
import numpy as np

def newtons_method(x):
    
    for i in range(10):
        x = x - f(x)/fprim(x)
        
        
    return x


def f(x):
    return 3*x**2

def fprim(x):
    return 6*x


x0 = 2
zero1 = newtons_method(x0) 
print(zero1)