# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:49:51 2020

@author: rishabhsaxena01
"""

a,b = list(map(int, input().split()))
if a <= 23 and b >=500 and b<=1000:
    print('Take Medicine')
else:
    print('Don\'t take Medicine')