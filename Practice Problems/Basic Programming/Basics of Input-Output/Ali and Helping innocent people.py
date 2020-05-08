# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:20:50 2020

@author: rishabhsaxena01
"""

vowel = ["A","E","I","O","U","Y"]
st = input()

if st[2] in vowel:
    result2 = False
else:
    result2 = True

if ((int(st[3]) + int(st[4]))%2==0) and ((int(st[4]) + int(st[5]))%2==0) and ((int(st[7] )+ int(st[8]))%2==0) and ((int(st[0])+int(st[1]))%2 ==0):
    result1 = True
else:
    result1 = False

if result1 and result2:
    print('valid')
else:
    print('invalid')