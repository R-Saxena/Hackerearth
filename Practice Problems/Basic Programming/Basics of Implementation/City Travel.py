# -*- coding: utf-8 -*-
"""
Created on Mon May 25 02:08:03 2020

@author: rishabhsaxena01
"""

s,x,n=input().split()
s=int(s)
x=int(x)
n=int(n)
t=[]
v=[]
for i in range(0,n):
    y,z=input().split()
    y=int(y)
    z=int(z)
    t.append(y)
    v.append(z)
z=sum(v)
s=s-z
if s>0:
    if s%x==0:
        count=n+int(s/x)
    else:
        count=n+int(s/x)+1
    print(count)
else:
    s=s+z
    i=1
    while s>0:
        try:
            q=t.index(i)
            s=s-v[q]
            i=i+1
        except ValueError:
            s=s-x
            i=i+1
    print(i-1)