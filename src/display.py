# -*- coding: utf-8 -*-
"""
Displays cars for given postions

"""
import numpy as np
from tkinter import *

class car_sprite:
    def __init__(self, canvas, position, radius):
        pos = tranformPosition(position,radius)
        self.radius = radius
        self.canvas = canvas
        self.car = canvas.create_rectangle(*pos,
            fill="red")

    def move(self,position):
        pos = tranformPosition(position,self.radius)
        dx = pos[0] - self.canvas.coords(self.car)[0]
        dy = pos[1] - self.canvas.coords(self.car)[1]
        self.canvas.move(self.car,dx,dy)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

def tranformPosition(position,radius):
    x1 = radius * np.cos(2*np.pi/1000 * position) + 240
    y1 = radius * np.sin(2*np.pi/1000 * position) + 240
    x2 = x1 + 20
    y2 = y1 + 20
    return x1,y1,x2,y2


class display:
    def __init__(self, num_of_cars,positions):
        self.root = Tk()
        self.root.title("Traffic Simulation")
        self.root.resizable(False,False)
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.create_circle(250, 250, 200, outline="#DDD", width=4)
        self.canvas.pack()

        self.cars = np.empty(num_of_cars,dtype=object)
        for i in range(self.cars.size):
            self.cars[i] = car_sprite(self.canvas,positions[i],200)
        self.canvas.update()

    def update(self,positions):
        for i in range(self.cars.size):
            self.cars[i].move(positions[i])
        self.canvas.update()
        self.canvas.after(15)


