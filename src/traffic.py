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
num_of_cars = np.array([3,4,3])
street_length = 1000
lanes = 3
h = 0.1

def main():
    c = car.intellgentDriver(2, 120 / 3.6, 4, 1, 1.5, 1, street_length)
    traffic_position = np.array([np.linspace(100,street_length -500,num_of_cars[0]),
                                 np.linspace(100,street_length -500,num_of_cars[1]),
                                 np.linspace(100,street_length -500,num_of_cars[2])])
    traffic_velocity = []
    for i in range(lanes):
        traffic_velocity.append(np.zeros(num_of_cars[i]) + 120 / 3.6)
    traffic_velocity = np.array(traffic_velocity)
    
    traffic = np.array([traffic_position,traffic_velocity])
    time_steps = 10000;
    plt.ion()
    plt.show()
    visualization(traffic[0])
    for i in range(time_steps):
        traffic = nums.rk4(h, traffic,[ c.velocity,c.accelaration],[[],[]])
        traffic[0] = traffic[0] % street_length;
        if i%3 == 0:
            visualization(traffic[0])
    return 0
    
def visualization(pos):
    plt.cla()
    plt.xlim(0,1000)
    plt.scatter(pos,np.ones(len(pos))) 
    plt.draw()
    plt.pause(1e-6)
    
def calcSurrounding(traffic_position):
    surrounding = []
    for i in range(traffic_position.shape[0]):
        surrounding.append([])
        for k in range(len(traffic_position[i])):
             surrounding[i].append(np.zeros(7))
             surrounding[i][k][0] = k
             surrounding[i][k][1] = (k+1) % len(traffic_position[i])
             surrounding[i][k][2] = (k-1) % len(traffic_position[i])
             
             if i == 0:
                surrounding[i][k][3] = -1
                surrounding[i][k][4] = -1             
             else:
                 Abstand = traffic_position[i][k] - traffic_position[i-1][0]
                 for l in range(len(traffic_position[i-1])): 
                     if traffic_position[i][k] - traffic_position[i-1][l] < 0 and traffic_position[i][k] - traffic_position[i-1][l] >= Abstand:
                         Abstand = traffic_position[i][k] - traffic_position[i-1][l]
                         front = l
                         back = l-1
                     else:
                         front = 0
                         back = len(traffic_position[i-1])
                 surrounding[i][k][3] = front
                 surrounding[i][k][4] = back
                 
             if i == traffic_position.shape[0] - 1:
                surrounding[i][k][5] = -1
                surrounding[i][k][6] = -1             
             else:
                 Abstand = traffic_position[i][k] - traffic_position[i+1][0]
                 for l in range(len(traffic_position[i+1])): 
                     if traffic_position[i][k] - traffic_position[i+1][l] < 0 and traffic_position[i][k] - traffic_position[i+1][l] >= Abstand:
                         Abstand = traffic_position[i][k] - traffic_position[i+1][l]
                         front = l
                         back = l-1
                     else:
                         front = 0
                         back = len(traffic_position[i-1])
                 surrounding[i][k][5] = front
                 surrounding[i][k][6] = back
    return surrounding
main()
