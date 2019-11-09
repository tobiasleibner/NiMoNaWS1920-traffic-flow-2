# -*- coding: utf-8 -*-
"""
Implementation of the car behavior.

"""
import numpy as np
from scipy.ndimage.interpolation import shift

class intellgentDriver:
    def __init__(self,
            opt_distant,
            opt_velocity   ,
            acc_coefficient,
            accelleration   ,
            acc_delay       ,
            follow_time     ,
            street_length   ):
        self.opt_distant     = opt_distant     
        self.opt_velocity    = opt_velocity    
        self.acc_coefficient = acc_coefficient 
        self.acc_const       = accelleration   
        self.acc_delay       = acc_delay       
        self.follow_time     = follow_time  
        self.street_length   = street_length
       
    def velocity(self,position,velocity):
        return velocity[0]

    def accelaration(self, position, velocity):
        return self.idm(position, velocity)
    
    def iidm(self, traffic):
        z = self.optimalDistant(traffic) / self.calcdistant(traffic)
        limit_idm = self.acc_const * ( 1 - ( self.speed / self.opt_velocity )**self.acc_coefficient)
        if z >= 1: 
            return self.acc_const * (1-z**2)
        return limit_idm * (1-z**(2*self.acc_coefficient/limit_idm))

    def idm(self,position, velocity):
        temp = self.acc_const * ( 1 - ( velocity[0] / self.opt_velocity )**self.acc_coefficient 
                                    - ( self.optimalDistant(velocity) / self.calcdistant(position))**2 )
        return self.acc_const * ( 1 - ( velocity[0] / self.opt_velocity )**self.acc_coefficient 
                                    - ( self.optimalDistant(velocity) / self.calcdistant(position))**2 )

    def optimalDistant(self, velocity):
        positiv = velocity[0] * self.follow_time + velocity[0] * self.calcVelocityDiff(velocity) / (2 * np.sqrt(self.acc_const * self.acc_delay))
        if positiv < 0: 
           return  self.opt_distant
        return self.opt_distant + positiv

    def calcdistant(self, position):
        return abs(position[0] - position[1]) % self.street_length

    def calcVelocityDiff(self, velocity):
        return velocity[0] - velocity[1]
