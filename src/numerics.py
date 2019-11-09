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

def rk4(h,traffic): 
    k = np.zeros([5,traffic.size])
    k2 = np.zeros([5,traffic.size])
    for n in range(traffic.size):
        for i in range(4):
            k[i+1][n] = traffic[n].velocity(traffic,
                traffic[n].position + h*b[i]*k[i][n],traffic[n].speed + h*b[i]*k2[i][n])
            k2[i+1][n] = traffic[n].accelaration(traffic,
                traffic[n].position + h*b[i]*k[i][n],traffic[n].speed + h*b[i]*k2[i][n])

    for i in range(traffic.size):
        for j in range(1,5):
            traffic[i].position = traffic[i].position + h * c[j] * k[j][i]
            traffic[i].speed = traffic[i].speed + h * c[j] * k[j][i]
    return traffic

