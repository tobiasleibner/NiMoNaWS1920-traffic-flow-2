import numpy as np 


b = [0,1/2,1/2,1]
c = [0,1/6,1/3,1/3,1/6]


def rk4(car_position,car_velocity,f,f1,h,num_of_cars): 
    k = np.zeros(5)
    k1 = np.zeros(5)
    place = np.zeros(num_of_cars)
    velocity = np.zeros(num_of_cars)
    
    for n in range(num_of_cars):
        for i in range(4):
            place[n] = car_position[n] + h * b[i]*k[i]
            velocity[n] = car_velocity[n] + h * b[i]*k1[i]
        
            k[i+1] = f(place[n],velocity[n],place[(n+1) % num_of_cars],velocity[(n+1) % num_of_cars])
            k1[i+1] = f1(place[n],velocity[n],place[(n+1) % num_of_cars],velocity[(n+1) % num_of_cars])
    
        for j in range(1,5):    
            car_position += h *c[j] *k[j]
            car_velocity += h *c[j] *k1[j]
            
    return(car_position,car_velocity)



