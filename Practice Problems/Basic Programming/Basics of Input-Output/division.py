# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:21:27 2020

@author: rishabhsaxena01
"""

def solve (A):
    no = ''
    for i in range(N):
        if i < N/2:
            no += A[i][0]
        else:
            no += A[i][-1]


    # print(no)
    if int(no)%11==0:
        return 'OUI'
    else:
        return 'NON'



N = int(input())
A = input().split()

out_ = solve(A)
print (out_)