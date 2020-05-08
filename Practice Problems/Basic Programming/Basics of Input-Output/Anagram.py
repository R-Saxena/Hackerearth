# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:37:55 2020

@author: rishabhsaxena01
"""

n=int(input())
for _ in range(n):
    a = input()
    b = input()
    m = len(a)+len(b)
    c=0
    for i in a:
        if i in b:
            c+=1
            b = b.replace(i, '',1)
    print(m - 2*c)