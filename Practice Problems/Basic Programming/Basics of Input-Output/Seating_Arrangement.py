# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:35:02 2020

@author: rishabhsaxena01
"""

def get_seat_type(n):
    seat = ['WS', 'MS', 'AS', 'AS', 'MS', 'WS']
    return seat[(n-1)%6]

def get_remainder(n):
    li = [-11, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9]
    r = n%12
    return n + li[r]
    
t = int(input())
for i in range(0,t):
    n = int(input())
    print("{} {}".format(get_remainder(n), get_seat_type(n)))
