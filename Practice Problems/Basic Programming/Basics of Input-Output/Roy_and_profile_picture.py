# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:45:36 2020

@author: rishabhsaxena01
"""

L = int(input())
n = int(input())
for _ in range(n):
    W,H = list(map(int, input().split()))

    if W >= L and H >= L:
        if W==H:
            print('ACCEPTED')
        else:
            print('CROP IT')
    else:
        print('UPLOAD ANOTHER')