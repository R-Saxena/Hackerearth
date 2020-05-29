# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:24:52 2020

@author: rishabhsaxena01
"""

def dfs(x,edge,queue,explored):
    if not explored[x]:
        queue.append(x)
        explored[x]=True
        for i in edge[x]:
            if explored[i]:
                continue
            dfs(i,edge,queue,explored)
            queue.append(x)
    else:
        return
    
n,m=map(int,input().split())
edge=[[] for i in range(n+1)]
explored=[False]*(n+1)
while m>0:
    m-=1
    x,y=map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)
queue=[]
dfs(1,edge,queue,explored)
print(len(queue))
print(*queue,sep=' ')