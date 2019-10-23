# -*- coding: utf-8 -*-
"""
Implementation of functions for solving numerically differential equations.

"""
import numpy as np 
import matplotlib.pyplot as plt

v_opt = 5
tau = 1
b = [0,1/2,1/2,1]
c = [0,1/6,1/3,1/3,1/6]

def rk4(h,value): 
    k = np.zeros(5)
    for i in range(4):
        k[i+1] = f(value + h * b[i]*k[i])
    for j in range(1,5):
        value = value +h *c[j] *k[j]
    return value

def f(v):
    func_value = (v_opt - v)/tau
    return func_value

