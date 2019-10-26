# -*- coding: utf-8 -*-
"""
Implementation of the car behavior.

"""
import numpy as np
from scipy.ndimage.interpolation import shift

class intellgentDriver:
    def __init__(self, opt_distant,
            opt_velocity   ,
            acc_coefficient,
            accelleration   ,
            acc_delay       ,
            follow_time):
       self.opt_distant     = opt_distant     
       self.opt_velocity    = opt_velocity    
       self.acc_coefficient = acc_coefficient 
       self.acc_const       = accelleration   
       self.acc_delay       = acc_delay       
       self.follow_time     = follow_time     

    def velocity(self, cars_position, cars_velocity):
        return cars_velocity
    def accelaration(self, cars_position, cars_velocity, L):
        return self.acc_const * ( 1 - ( cars_velocity / self.opt_velocity )**self.acc_coefficient 
                                    - ( optimalDistant(cars_velocity) / calcdistant(cars_position, L ))**2 )
    
    def optimalDistant(self, cars_velocity):
        return self.opt_distant + np.max([0,cars_velocity * self.follow_time + cars_velocity * calcVelocityDiff(cars_velocity) / (2 * np.sqrt(self.acc_const * self.acc_delay))])

def calcdistant(cars_position,lenght):
    last_element = cars_position[0] - cars_position[-1]
    dist = np.append(np.diff(cars_position),last_element)
    dist[dist  < 0 ] = dist[dist < 0] + lenght - 2*cars_position[np.roll(dist<0,1)]
    return dist

def calcVelocityDiff(cars_velocity):
    last_element = cars_velocity[0] - cars_velocity[-1]
    diff = np.append(np.diff(cars_velocity),last_element)
    diff = np.abs(diff)
    return diff