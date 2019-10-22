# -*- coding: utf-8 -*-
"""
Implementation of functions for solving numerically differential equations.

"""
import numpy as np 
import matplotlib.pyplot as plt


def euler(stepsize,value,func_value): 
    return value + stepsize * func_value
