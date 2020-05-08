# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:55:09 2020

@author: rishabhsaxena01
"""

n = input()
if len(n) != 10:
    print('Illegal ISBN')
else:
    c=0
    for i in range(1,len(n)+1):
        c = c + i*int(n[i-1])
    if c%11 ==0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')