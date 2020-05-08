# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:19:45 2020

@author: rishabhsaxena01
"""

t= int(input())
for _ in range(t):
    n = int(input())
    for i in range(n-1, -1, -1):
        for j in range(0,n-i):
            print('*',end= "")
            
        for j in range(0,2*i):
            print('#', end = "")
        
        for j in range(0,n-i):
            print('*', end = "")
        
        print('\n')
            
        