# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:40:33 2020

@author: rishabhsaxena01
"""

t = input()
ans = 1
li = list(map(int, input().split()))
for i in li:
    ans = ans*i 
limit = 10**9+7
print(ans%limit)