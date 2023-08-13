# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 12:10:17 2023

@author: Yead
"""

def number(bus_stops):
    '''
    bus_stops: a list (or array) of integer pairs
        x =  number of people that get on the bus
        y =  number of people that get off the bus
    return: the number of people who are still on the bus
    number([[10,0],[3,5],[5,8]]) -----> 5
    '''
    x = 0 # sum of on and of the bus 
    for i in bus_stops:
        x += i[0] - i[1]
    return x
