# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:29:36 2020

@author: rishabhsaxena01
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

step = 0
flag = True
m = min(a)
while True:
    change = False
    for i in range(n):
        if a[i] > m:
            if a[i] >= b[i]:
                a[i] = a[i] - b[i]
                m = min(a[i],m)
                step +=1
                change = True
            else:
                flag = False
                break;

    if not flag or not change:
        break;

if flag:
    print(step)
else:
    print('-1')