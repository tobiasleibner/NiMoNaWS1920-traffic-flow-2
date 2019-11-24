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
cars_per_lane = np.array([10])
street_length = 1000
lanes = 1
h = 0.1
time_steps = 10000;

class trafficSpace():
    def __init__(self,position,velocity,cars_per_lane,driver):
        self.velocity    = np.ones(position.size) * velocity
        self.position    = position
        self.lanes       = self.transformLines(cars_per_lane)
        self.surrounding = self.calcSurrounding(position,cars_per_lane)
        self.driver      = driver
        self.size        = position.size

    def calcSurrounding(self,traffic_position,cars_per_lane):
        surrounding = np.zeros([traffic_position.size,7],dtype = int)
        cars_offset = 0
        for i in range(cars_per_lane.shape[0]):
            for k in range(cars_per_lane[i]):
                surrounding[k + cars_offset][0] = k + cars_offset
                surrounding[k + cars_offset][1] = (k + 1) % cars_per_lane[i] + cars_offset
                surrounding[k + cars_offset][2] = (k - 1) % cars_per_lane[i] + cars_offset
            cars_offset = cars_offset + cars_per_lane[i]
        return surrounding

    def transformLines(self,cars_per_lane):
        result = np.zeros(int(cars_per_lane[0]))
        for i in range(1,cars_per_lane.shape[0]):
            result = np.concatenate((result,np.ones(int(cars_per_lane[i]))*i))
        return result

def main():
    traffic_position = np.linspace(100,street_length -800,cars_per_lane[0])
    for i in range(1,lanes):
        traffic_position = np.concatenate((traffic_position,np.linspace(100 ,
            street_length - 500, cars_per_lane[i])), axis=None)
    driver = np.empty(sum(cars_per_lane),dtype=object)
    maxspeeds = np.ones(10) *120 / 3.6
    maxspeeds[5] = 80 / 3.6
    for i in range(driver.size):
        driver[i] = car.intellgentDriver(2, maxspeeds[i], 4, 1, 1.5, 1, street_length)

    traffic = trafficSpace(traffic_position,120/3.6,cars_per_lane,driver)

    
    plt.ion()
    plt.show()
    visualization(traffic.position,traffic.lanes)
    for i in range(time_steps):
        traffic = nums.rk4(h, traffic)
        traffic.position = traffic.position % street_length
        if i%3 == 0:
            visualization(traffic.position,traffic.lanes)
    return 0



def visualization(pos,lanes):
    plt.cla()
    plt.xlim(0,1000)
    plt.scatter(pos,lanes) 
    plt.draw()
    plt.pause(0.01)
    


main()
