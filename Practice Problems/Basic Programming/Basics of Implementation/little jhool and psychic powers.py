# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:50:34 2020

@author: rishabhsaxena01
"""

max_c = 0
s=0
st = input()
for i in range(len(st)-1):
    if st[i+1] == st[i]:
        s +=1
    else:
        s=0
    if max_c < s:
        max_c = s

if max_c >= 5:
    print('Sorry, sorry!')
else:
    print('Good luck!')