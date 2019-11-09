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
    num_eq,num_dimension = value.shape
    k = np.zeros([5,num_eq,num_dimension])
    arg = [None] * num_eq
    for i_arg in range(num_eq):
        arg[i_arg] = [None] * num_eq + add_args[i_arg]

    for i in range(4):
        for i_arg in range(num_eq):
            for n_arg in range(num_eq):
                arg[i_arg][n_arg] = value[n_arg] + h * b[i] * k[i][n_arg]

        for n in range(num_eq):
            k[i+1][n] = func[n](*arg[n])

    for i in range(num_eq):
        for j in range(1,5):
            value[i] = value[i] + h * c[j] * k[j][i]
    return value

