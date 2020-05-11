# -*- coding: utf-8 -*-
"""
Created on Tue May 12 02:20:34 2020

@author: rishabhsaxena01
"""

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    print(int(max(a,b)/min(a,b)))