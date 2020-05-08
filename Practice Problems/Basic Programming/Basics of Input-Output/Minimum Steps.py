# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:49:50 2020

@author: rishabhsaxena01
"""

def f(k,m,n):
    if k >= m:
        return((k-m)//2 + (k-m)%2)

    if m % n == 0:
        return (1 + f(k, m//n, n))
    else:
        x = (m//n + 1)*n;
        return ((x-m)//2 + (x-m)%2 + f(k, x, n))

t = int(input())
while t > 0:
    a, b, c = map(int, input().split())
    print(f(a, b, c))
    t -= 1