# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:01:18 2020

@author: rishabhsaxena01
"""

for _ in range(int(input())):
    n = int(input())
    while n>0:
        if n%2==0:
            n=n//2
        else:
            n= 3*n+1
        if n==1:
            break
    
    if n==1:
        print('YES')
    else:
        print('NO')