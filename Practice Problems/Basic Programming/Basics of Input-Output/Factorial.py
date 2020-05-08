# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:43:04 2020

@author: rishabhsaxena01
"""

def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))

print(fact(int(input())))