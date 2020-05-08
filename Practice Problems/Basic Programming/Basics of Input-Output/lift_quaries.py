# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:49:00 2020

@author: rishabhsaxena01
"""

a = 0
b = 7
n = int(input())
for _ in range(n):
    x = int(input())
    if abs(a-x) <= abs(b-x):
        print('A')
        a = x
    else:
        print('B')
        b = x