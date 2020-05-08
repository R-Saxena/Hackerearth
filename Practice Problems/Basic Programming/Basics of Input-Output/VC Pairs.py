# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:18:54 2020

@author: rishabhsaxena01
"""
vowel = ['a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
    n = int(input())
    st = input()
    c = 0
    for i in range(n-1):
        if st[i] not in vowel and st[i+1] in vowel:
            c+=1
    
    print(c)