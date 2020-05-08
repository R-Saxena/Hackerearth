# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:42:19 2020

@author: rishabhsaxena01
"""

count = 0
a,b,c = list(map(int, input().split()))
for i in range(a,b+1):
    if i %c ==0:
        count+=1

print(count)