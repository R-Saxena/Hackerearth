# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:14:23 2020

@author: rishabhsaxena01
"""

t = input()
c=0
for i in t:
    c += ord(i)-ord('a')+1
print(c)