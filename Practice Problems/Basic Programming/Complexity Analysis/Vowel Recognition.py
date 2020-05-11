# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:30:46 2020

@author: rishabhsaxena01
"""


for _ in range(int(input())):
    S = input()
    s=0
    for j in range(len(S)):
        if S[j].lower() in 'aeiou':
            s = s + ((j+1)*(len(S)-j))
    print(s)





