# -*- coding: utf-8 -*-
"""
Implementation of the simulation.

"""
import numpy as np 
import matplotlib.pyplot as plt
import car
import numerics as nums

# Parameters 
# System
num_of_cars     = 10
street_length   = 1000
traffic = np.empty(num_of_cars)
h = 0.01

def main():
    c = car.intellgentDriver(2, 120 / 3.6, 4, 8, 1.5, 1)
    traffic_position = np.linspace(10,street_length -10,num_of_cars)
    traffic_velocity = np.zeros(num_of_cars) + 120 / 3.6
    traffic = np.array([traffic_position,traffic_velocity])
    time_steps = 10000;
    plt.ion()
    plt.show()
    visualization(traffic[0])
    for i in range(time_steps):
        traffic = nums.rk4(h, traffic,[ c.velocity,c.accelaration],[[],[street_length]])
        traffic[0] = traffic[0] % street_length;
        if i%10 == 0:
            visualization(traffic[0])
    return 0
    
def visualization(pos):
    plt.cla()
    plt.xlim(0,1000)
    plt.scatter(pos,np.ones(len(pos))) 
    plt.draw()
    plt.pause(1e-6)
    

main()
