# -*- coding: utf-8 -*-
"""
Created on Sat May  9 01:10:49 2020

@author: rishabhsaxena01
"""

n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
ans = -1
value = float('inf')
for i in range(n):
    if (total-arr[i])%7 ==0:
        if value > arr[i]:
            value= arr[i]
            ans = i

print(ans)