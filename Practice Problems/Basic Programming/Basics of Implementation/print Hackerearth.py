# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:10:33 2020

@author: rishabhsaxena01
"""

N = int(input())
st = input()
li = [0,0,0,0,0,0,0]   #h a c k e r t
for i in st:
    if i =='h':
        li[0]+=1
    elif i == 'a':
        li[1]+=1
    elif i == 'c':
        li[2]+=1 
    elif i == 'k':
        li[3]+=1  
    elif i == 'e':
        li[4]+=1
    elif i == 'r':
        li[5]+=1
    elif i == 't':
        li[6]+=1

print(min( int(li[0]/2), int(li[1]/2), li[2], li[3], int(li[4]/2), int(li[5]/2), li[6]))