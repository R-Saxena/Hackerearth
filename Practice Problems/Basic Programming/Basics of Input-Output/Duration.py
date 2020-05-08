# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:03:16 2020

@author: rishabhsaxena01
"""

for _ in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    diff = (c*60 + d) - (a*60 + b) 
    x = int(diff/60)
    y = diff%60
    print(x, y)