# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:45:00 2020

@author: rishabhsaxena01
"""

n = int(input())
Limit = int(input())
for _ in range(n):
    x = int(input())
    if (x >= Limit):
        print('YES')
    else:
        print('NO')