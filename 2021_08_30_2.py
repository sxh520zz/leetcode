#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:43 2021

@author: shixiaohan
"""


class Solution:
    def combine(n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        '''
        path = []
        res = []
        def check(path):
            for i in range(len(path)-1,0,-1):
                if(path[i]> path[i-1]):
                    continue
                else:
                    return False
            return True
            
        def backtrack(n,k):
            if(len(path) == k):
                if(check(path)):
                    res.append(path[:])
                return
            for i in range(1,n+1):
                if i in path:
                    continue
                path.append(i)
                backtrack(n,k)
                path.pop()
        backtrack(n,k)
        
        return res
        '''
        res = []
        path = []

        def backtrace(idx):
            nonlocal res
            nonlocal path
            if len(path) == k:
                res.append(path[:])
                return
            if idx == n + 1:
                return 
                
            backtrace(idx + 1)

            path.append(idx)
            backtrace(idx + 1)
            path.pop()

        backtrace(1)
        return res

        
n = 5
k = 3

print(Solution.combine(n, k))