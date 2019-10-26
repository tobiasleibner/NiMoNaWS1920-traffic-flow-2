# -*- coding: utf-8 -*-
"""
Implementation of the simulation.

"""
import numpy as np 
import matplotlib.pyplot as plt
import car
import numerics as nums


def main():
    # Parameter für beliebig viele Autos
    num_of_cars = 2
    car_position = np.arange(num_of_cars)
    car_velocity = np.zeros(num_of_cars)
    
    #Parameter für das intelligent-driver-model
    a = 1
    v_0 = 120/3.6
    delta = 4
    s_0 = 2
    T = 1
    a = 1
    b = 1.5
    
    #Parameter des Runge-Kutta-Algorithmuses
    h = 0.01
    
    #Parameter der Visualisierung
    Zeitschritt = 100
      
    for i in range(Zeitschritt): 
        Delta_v,s = car.Abstand(car_position,car_velocity,num_of_cars)
        car_position,car_velocity = nums.rk4(car_position,car_velocity,car.intellegent_driver_model(car_velocity,v_0,s,s_0,delta,Delta_v,T,a,b),car.Ort(car_velocity),h,num_of_cars,v_0,s,s_0,delta,Delta_v,T,a,b)                                  
        visualization(Zeitschritt,car_position)      
    return 0

    
def visualization(Zeitschritt,car_position):
    plt.ion()        
    plt.title("intelligent-driver-model")
    plt.plot(car_position,0)
    plt.pause(0.001)     
    plt.ioff
    return 0

main()