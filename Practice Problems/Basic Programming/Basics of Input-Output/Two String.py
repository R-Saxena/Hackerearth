# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:57:25 2020

@author: rishabhsaxena01
"""

t = int(input())
for _ in range(t):
    x = 'YES'
    a,b = input().split()
    for i in a:
        if i not in b:
            x = 'NO'
            break
        b = b.replace(i,"",1)
    
    print(x)
