# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:09:59 2020

@author: rishabhsaxena01
"""

st = input()
s = 0
max_s =0
for i in range(len(st)-1):
    if st[i] !=st[i+1]:
        s+=1
    else:
        s=0
    
    if max_s < s:
        max_s = s

print(max_s+1)