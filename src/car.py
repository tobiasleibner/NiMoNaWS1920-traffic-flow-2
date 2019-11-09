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
            follow_time     ,
            street_length   ,
            surrounding):
       self.opt_distant     = opt_distant     
       self.opt_velocity    = opt_velocity    
       self.acc_coefficient = acc_coefficient 
       self.acc_const       = accelleration   
       self.acc_delay       = acc_delay       
       self.follow_time     = follow_time  
       self.street_length   = street_length 
       self.surrounding     = surrounding
       
    def velocity(self, cars_position, cars_velocity):
        return cars_velocity
    def accelaration(self, cars_position, cars_velocity):
        return self.idm(cars_position, cars_velocity)
    
    def iidm(self, cars_position, cars_velocity):
        z = self.optimalDistant(cars_velocity) / calcdistant(cars_position, self.street_length)
        result = np.empty(len(z))
        limit_idm = self.acc_const * ( 1 - ( cars_velocity / self.opt_velocity )**self.acc_coefficient)
        result[z >= 1] = self.acc_const * (1-z[z >= 1]**2)
        result[z < 1] = limit_idm[z < 1] * (1-z[z < 1]**(2*self.acc_coefficient/limit_idm[z < 1]))

        return  result

    def idm(self, cars_position, cars_velocity):
        return self.acc_const * ( 1 - ( cars_velocity / self.opt_velocity )**self.acc_coefficient 
                                    - ( self.optimalDistant(cars_velocity) / calcdistant(cars_position, self.street_length ))**2 )

    def optimalDistant(self, cars_velocity):
        positiv = cars_velocity * self.follow_time + cars_velocity * calcVelocityDiff(cars_velocity) / (2 * np.sqrt(self.acc_const * self.acc_delay))
        positiv[positiv < 0] = 0
        return self.opt_distant + positiv

    def calcdistant(self, cars_position):
        last_element = cars_position[0] - cars_position[-1]
        dist = np.append(np.diff(cars_position),last_element)
        dist[dist  < 0 ] = dist[dist < 0] + lenght
        return dist

def calcVelocityDiff(cars_velocity):
    last_element = cars_velocity[0] - cars_velocity[-1]
    diff = np.append(np.diff(cars_velocity),last_element)
    diff = np.abs(diff)
    return diff

class car:
    def __init__(self, opt_distant,
            opt_velocity   ,
            acc_coefficient,
            accelleration   ,
            acc_delay       ,
            follow_time     ,
            street_length   ,
            surrounding):
       self.opt_distant     = opt_distant     
       self.opt_velocity    = opt_velocity    
       self.acc_coefficient = acc_coefficient 
       self.acc_const       = accelleration   
       self.acc_delay       = acc_delay       
       self.follow_time     = follow_time  
       self.street_length   = street_length 
       self.surrounding     = surrounding