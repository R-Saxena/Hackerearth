# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:55:51 2020

@author: rishabhsaxena01
"""


def cal_max_index(tsum):
    n = (-1+(1+(4*2*tsum))**(1/2))/2
    n = int(n)
    return int((n*(n+1)/2))-1
 
    
n = int(input())
inarr =list(map(int, input().split()))
#print(inarr)
sumarr = []
sumv = 0
for a in inarr:
    sumv = sumv+a
    sumarr.append(sumv)
 
maxspsum = 0
spind = 0
 
for i in range(n):
    tsum = n-i
    series_max_n = cal_max_index(tsum)
    if i ==0 :
        maxspsum = sumarr[series_max_n]
    else:
        ser_sum = sumarr[series_max_n+i]-sumarr[i-1]
        if ser_sum > maxspsum:
            maxspsum = ser_sum
print(maxspsum)
