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
num_of_cars     = 3
street_length   = 1000
traffic = np.empty(num_of_cars)
h = 0.001

def main():
    c = car.intellgentDriver(2, 120 / 3.6, 4, 1, 1.5, 1)
    traffic_position = np.linspace(0,1000,num_of_cars)
    traffic_velocity = np.zeros(num_of_cars) + 50
    traffic = np.array([traffic_position,traffic_velocity])
    print(traffic.shape)
    time_steps = 100;
    plt.ion()
    plt.show()
    visualization(traffic[0])
    for i in range(time_steps):
        traffic = nums.rk4(h, traffic,[ c.velocity,c.accelaration],[[],[street_length]])
        traffic[0] = traffic[0] % street_length;
    return 0
    
def visualization(pos):
    plt.scatter(pos,np.ones(len(pos))) 
    plt.draw()


main()
