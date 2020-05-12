# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:00:14 2020

@author: rishabhsaxena01
"""

for _ in range(int(input())):
    x = int(input())
    sqrt_i = int(x ** (0.5))
    l = len(bin(sqrt_i)) - 3
    invalid_result = 2 ** (l+1)
    invalid_divisor_result = x // invalid_result
    invalid_divisor = (2 ** (l)) - 1
    max_invalid = max(invalid_divisor, invalid_divisor_result)
    print(x - max_invalid)