# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:38:50 2020

@author: rishabhsaxena01
"""

def palin(a):
    for i in range(len(a)):
            k= len(a)-1-i
            if i>=k:
                break
            if a[i] != a[k]:
                return 'NO'
    return 'YES'

print(palin(input()))