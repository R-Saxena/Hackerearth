# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:48:11 2020

@author: rishabhsaxena01
"""

n = int(input())
i=1
while True:
    if i >= n:
        print('Patlu')
        break
    else:
        n=n-i
    
    if 2*i >= n:
        print('Motu')
        break
    else:
        n=n-2*i
    
    i+=1