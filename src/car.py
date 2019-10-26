import numpy as np


def Ort(v):
    return v

def intellegent_driver_model(v,v_0,s,s_0,delta,Delta_v,T,a,b): 
    
    s_star = s_0 + np.max(0,v*T + (v*Delta_v)/(2*(a*b)**0.5))  
    driver = a*(1 - (v/v_0)**delta - (s_star(v,Delta_v)/s)**2)  
    
    return driver

def Abstand(car_position,car_velocity,num_of_cars):
    for n in range(num_of_cars):
        Delta_v = np.zeros(num_of_cars)
        s = np.zeros(num_of_cars)
    
        Delta_v[n] = abs(car_velocity[(n+1) % num_of_cars] - car_velocity[n]) 
        s[n] = abs(car_position[(n+1) % num_of_cars] - car_position[n])
        
    return Delta_v,s
 
