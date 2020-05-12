# -*- coding: utf-8 -*-
"""
Created on Tue May 12 06:23:04 2020

@author: rishabhsaxena01
"""

for _ in range(int(input())):
    a,b = list(map(int, input().split()))
    if b%a ==0:
        print('Yes')
    else:
        print('No')