# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:29:15 2020

@author: rishabhsaxena01
"""

while True:
    try:
        a,b = list(map(int, input().split()))
        print(a+b)
    except:
        break