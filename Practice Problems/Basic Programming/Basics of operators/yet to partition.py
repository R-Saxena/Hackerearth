# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:19:57 2020

@author: rishabhsaxena01
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    X=0
    for i in range(n):
        X ^= arr[i]
        
    mx = X
    fst = 0
    for i in range(n):
        fst ^= arr[i]
        scd = X ^ fst
        if (fst & scd) > mx:
            mx = fst & scd
        
    print(mx)