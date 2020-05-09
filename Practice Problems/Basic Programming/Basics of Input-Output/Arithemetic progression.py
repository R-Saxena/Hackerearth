# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:25:46 2020

@author: rishabhsaxena01
"""

for i in range(int(input())):
    a,b,c = list(map(int, input().split()))
    
    x = int((a+c)/2)
    if (a+c)%2 !=0 and b<=x:
        x = x+1
    print(abs(x-b))
