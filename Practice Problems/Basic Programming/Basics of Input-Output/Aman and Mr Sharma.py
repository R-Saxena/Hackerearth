# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:28:01 2020

@author: rishabhsaxena01
"""

c=0
for _ in range(int(input())):
    r,h = list(map(int, input().split()))
    if (100*h) >= (2*22*r/7):
        c+=1

print(c)