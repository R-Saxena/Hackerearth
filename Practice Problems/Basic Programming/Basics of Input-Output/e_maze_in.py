# -*- coding: utf-8 -*-
"""
Created on Fri May  8 06:47:27 2020

@author: rishabhsaxena01
"""

st = input()
L = st.count('L')
R = st.count('R')
U = st.count('U')
D = st.count('D')

a = R-L
b = U-D
print("{} {}".format(a,b))