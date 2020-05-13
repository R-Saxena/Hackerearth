# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:08:27 2020

@author: rishabhsaxena01
"""

n = input()
last = False
if n[-1] =='6':
    last = True
n = n.replace('6','')
l=0
for i in n:
    if i not in '123456':
        l = -1
        break
    else:
        l=l+1
if l <=0 or last:
    print(-1)
else:
    print(l)