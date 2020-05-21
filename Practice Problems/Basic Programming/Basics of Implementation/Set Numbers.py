# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:21:36 2020

@author: rishabhsaxena01
"""

for _ in range(int(input())):
    num = int(input())
    bi = len(bin(num)[2:])
    while bi > 0:
        i=int('1'*bi,2)
        if i<= num:
            print(i)
            break
        bi-=1
