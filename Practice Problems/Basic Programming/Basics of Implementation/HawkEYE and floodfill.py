# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:51:26 2020

@author: rishabhsaxena01
"""

size = int(input())
a,b,p = list(map(int, input().split()))
for i in range(size):
    for j in range(size):
            print(max(0,p - max(abs(i-a), abs(j-b))), end = ' ')
    print('')