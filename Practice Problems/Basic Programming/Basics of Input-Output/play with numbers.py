# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:32:12 2020

@author: rishabhsaxena01
"""

n,q = list(map(int, input().split()))
arr = list(map(int, input().split()))
sum_arr = [sum(arr[:i+1]) for i in range(n)]
for i in range(q):
    L,R = list(map(int, input().split()))
    total = R-L+1
    if L==1:
        print((sum_arr[R-1])//total)
    else:
        print((sum_arr[R-1] - sum_arr[L-2])//total)