import numpy as np 


b = [0,1/2,1/2,1]
c = [0,1/6,1/3,1/3,1/6]


def rk4(car_position,car_velocity,f,f1,h,num_of_cars,v_0,s,s_0,delta,Delta_v,T,a,b): 
    k = np.zeros(5)
    k1 = np.zeros(5)
    
    for n in range(num_of_cars):
        for i in range(4):
        
            k[i+1] = f(car_velocity[n] + h * b[i]*k1[i],v_0,s,s_0,delta,Delta_v,T,a,b)
            k1[i+1] = f1(car_velocity[n] + h * b[i]*k1[i])
    
        for j in range(1,5):    
            car_position += h *c[j] *k[j]
            car_velocity += h *c[j] *k1[j]
            
    return(car_position,car_velocity)



