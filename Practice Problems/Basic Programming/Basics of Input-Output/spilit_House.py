# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:46:39 2020

@author: rishabhsaxena01
"""

n = input()
x = input().replace('.', 'B')
b = 'YES'
for i in range(1,len(x)):
    if x[i] == 'H' and x[i-1] == 'H':
        b = 'NO'
print(b)
if b != 'NO':
    print(x)