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
cars_per_lane = np.array([3,4,3])
street_length = 1000
lanes = 3
h = 0.1
time_steps = 10000;

def main():
    traffic_position = np.linspace(100,street_length -500,cars_per_lane[0])
    for i in range(1,lanes):
        traffic_position = np.concatenate((traffic_position,np.linspace(100 ,
            street_length - 500, cars_per_lane[i])), axis=None)
    
    traffic = np.empty(sum(cars_per_lane),dtype=object)
    lane_of_car = transformLines(cars_per_lane)
    surrounding = calcSurrounding(traffic_position,cars_per_lane)
    for i in range(traffic.size):
        traffic[i] = car.intellgentDriver(traffic_position[i], 120/3.6, 
            lane_of_car[i], 2, 120 / 3.6, 4, 1, 1.5, 1, street_length, surrounding[i])

    plt.ion()
    plt.show()
    visualization(np.array([ x.position for x in traffic]),np.array([ x.lane for x in traffic]))
    for i in range(time_steps):
        traffic = nums.rk4(h, traffic)
        for x in traffic:
             x.position = x.position % street_length
        if i%3 == 0:
            visualization(np.array([ x.position for x in traffic]),np.array([ x.lane for x in traffic]))
    return 0

def transformLines(cars_per_lane):
    result = np.zeros(int(cars_per_lane[0]))
    for i in range(1,cars_per_lane.shape[0]):
        result = np.concatenate((result,np.ones(int(cars_per_lane[i]))*i))
    return result

def visualization(pos,lanes):
    plt.cla()
    plt.xlim(0,1000)
    plt.scatter(pos,lanes) 
    plt.draw()
    plt.pause(0.01)
    
def calcSurrounding(traffic_position,cars_per_lane):
    surrounding = np.zeros([traffic_position.size,7],dtype = int)
    cars_offset = 0
    for i in range(cars_per_lane.shape[0]):
        for k in range(cars_per_lane[i]):
            surrounding[k + cars_offset][0] = k + cars_offset
            surrounding[k + cars_offset][1] = (k + 1) % cars_per_lane[i] + cars_offset
            surrounding[k + cars_offset][2] = (k - 1) % cars_per_lane[i] + cars_offset
        cars_offset = cars_offset + cars_per_lane[i]
    return surrounding

main()
