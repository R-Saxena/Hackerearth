# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:21:55 2020

@author: rishabhsaxena01
"""

matchsticks = [6,2,5,5,4,5,6,3,7,6]
def get_machis(x):
    su = 0
    for i in x:
        su+=matchsticks[int(i)]
    
    return su

# Write your code here
for _ in range(int(input())):
    x = input()
    machis = get_machis(x)
    no = ''
    if machis%2==0:
        for i in range(int(machis/2)):
            no += '1'
    else:
        no+='7'
        for i in range(int(machis/2-1)):
            no += '1'
    print(no)