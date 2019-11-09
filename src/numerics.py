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

    for i in range(4):
        for n in range(traffic.size):
            surr = traffic.surrounding[n]
            k[i+1][n] = traffic.driver[n].velocity(
                traffic.position[surr] + h*b[i]*k[i][n], 
                traffic.velocity[surr] + h*b[i]*k2[i][n])
            k2[i+1][n] = traffic.driver[n].accelaration(
                traffic.position[surr] + h*b[i]*k[i][n], 
                traffic.velocity[surr] + h*b[i]*k2[i][n])

    for i in range(traffic.size):
        for j in range(1,5):
            traffic.position[i] = traffic.position[i] + h * c[j] * k[j][i]
            traffic.velocity[i] = traffic.velocity[i] + h * c[j] * k2[j][i]
    return traffic

