# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:20:44 2020

@author: rishabhsaxena01
"""

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

num = ['0', '1', '2', '3','4','5','6','7','8','9']
# Write your code here
text = input()
ans = ''
number = int(input())
for i in text:
    if i in cap:
        ans += cap[(cap.index(i)+number)%26]
    elif i in small:
        ans += small[(small.index(i)+number)%26]
    elif i in num:
        ans += num[(num.index(i)+number)%10]
    else:
        ans+=i

print(ans)