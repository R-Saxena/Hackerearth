# -*- coding: utf-8 -*-
"""
Created on Mon May 11 01:32:55 2020

@author: rishabhsaxena01
"""

prime_ascii_list = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def get_list(n):
    li = []
    for i in prime_ascii_list:
        li.append(abs(i-n))
    return li

for _ in range(int(input())):
    n = int(input())
    st = input()
    ans = ''
    for i in st:
        li = get_list(ord(i))
        ans += chr(prime_ascii_list[li.index(min(li))])
    
    print(ans)