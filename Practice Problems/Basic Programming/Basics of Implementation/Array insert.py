# -*- coding: utf-8 -*-
"""
Created on Tue May 12 02:33:17 2020

@author: rishabhsaxena01
"""

N,Q = list(map(int,input().split()))
arr = list(map(int,input().split()))
for i in range(Q):
    a,b,c = list(map(int,input().split()))
 
    if a==1:
        arr[b] = c
    else:
        print(sum(arr[b:c+1]))