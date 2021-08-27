#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:33:53 2021

@author: shixiaohan
"""

class Solution(object):
    def findCircleNum(isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        '''
        #my mistakes
        def dfs(i,j, y,isConnected):
            cnt = 1
            for w in range (y):
                if(w != j):
                    if(isConnected[j][w] == 1 and w != i):
                        cnt += dfs(j,w,y,isConnected)
            return cnt
        
        
        x = len(isConnected)
        y = len(isConnected[0])
        
        if(sum(isConnected[0]) == y):
            return 1
        else:
            all_part = 0
            for i in range (x):
                for j in range (y):
                    if isConnected[i][j] == 1 and i != j:
                        all_part += dfs(i,j,y,isConnected)
            return len(isConnected) -all_part 
        '''
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
        
        return circles

      
isConnected = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
               [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
               [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
               [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
               [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
print(Solution.findCircleNum(isConnected))