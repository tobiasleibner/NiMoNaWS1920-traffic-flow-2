# -*- coding: utf-8 -*-
"""
Implementation of the car behavior.

"""
import numpy as np
from scipy.ndimage.interpolation import shift

class intellgentDriver:
    def __init__(self,
            start_position,
            start_velocity,
            lane,
            opt_distant,
            opt_velocity   ,
            acc_coefficient,
            accelleration   ,
            acc_delay       ,
            follow_time     ,
            street_length   ,
            surrounding):
        self.speed           = start_velocity
        self.position        = start_position
        self.lane            = lane
        self.opt_distant     = opt_distant     
        self.opt_velocity    = opt_velocity    
        self.acc_coefficient = acc_coefficient 
        self.acc_const       = accelleration   
        self.acc_delay       = acc_delay       
        self.follow_time     = follow_time  
        self.street_length   = street_length 
        self.surrounding     = surrounding
       
    def velocity(self, traffic,pos,vel):
        return vel

    def accelaration(self, traffic,pos,vel):
        return self.idm(traffic)
    
    def iidm(self, traffic):
        z = self.optimalDistant(traffic) / self.calcdistant(traffic)
        limit_idm = self.acc_const * ( 1 - ( self.speed / self.opt_velocity )**self.acc_coefficient)
        if z >= 1: 
            return self.acc_const * (1-z**2)
        return limit_idm * (1-z**(2*self.acc_coefficient/limit_idm))

    def idm(self, traffic):
        return self.acc_const * ( 1 - ( self.speed / self.opt_velocity )**self.acc_coefficient 
                                    - ( self.optimalDistant(traffic) / self.calcdistant(traffic))**2 )

    def optimalDistant(self, traffic):
        positiv = self.speed * self.follow_time + self.speed * self.calcVelocityDiff(traffic) / (2 * np.sqrt(self.acc_const * self.acc_delay))
        if positiv < 0: 
           return  self.opt_distant
        return self.opt_distant + positiv

    def calcdistant(self, traffic):
        return abs(self.position - traffic[self.surrounding[1]].position) % self.street_length

    def calcVelocityDiff(self, traffic):
        return self.speed - traffic[int(self.surrounding[1])].speed-
