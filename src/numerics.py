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

def rk4(h,value,func,add_args): 
    num_eq = value.shape[0]
    k = np.zeros([num_eq,5])
    arg = [[None] * num_eq]*2
    for i_arg in range(num_eq):
        arg[i_arg].append(add_args[i_arg])

    for i in range(4):
        for i_arg in range(num_eq):
            arg[i_arg][0:num_eq] = value[i_arg] + h * b[i]*k[i_arg][i]

        for n in range(num_eq):
            k[n][i+1] = func[n](*arg)

    for i in range(num_eq):
        for j in range(1,5):
            value[i] = value[i] + h *c[j] *k[i][j]
    return value

