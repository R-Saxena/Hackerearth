# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:21:10 2020

@author: rishabhsaxena01
"""

from math import ceil,floor
# Write your code here
for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    # print(a,b,c)
    if c >=b:
        print(-1,-1)
    else:
        m = ceil(a/c)
        n = int(b/c)
        if m > n:
            print(-1,-1)
        else:
            print(int(m),int(n))