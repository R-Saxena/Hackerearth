# -*- coding: utf-8 -*-
"""
Created on Tue May 12 02:13:59 2020

@author: rishabhsaxena01
"""

a,b = input().split()
b = int(b)
a = list(a)
i=0
for i in range(len(a)):
    if a[i]!='9' and b!=0:
        a[i] = '9'
        b = b-1

print(''.join(a))