# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:40:50 2020

@author: rishabhsaxena01
"""

t = int(input())
for _ in range(t):
    a=0
    b=0
    g,p = list(map(int, input().split()))
    n = int(input())
    for _ in range(n):
        n1,n2 = list(map(int, input().split()))
        a = a+n1
        b =b+n2
    
    print(min(a*g+b*p, b*g+a*p))