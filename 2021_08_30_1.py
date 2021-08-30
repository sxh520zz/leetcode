#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:03:09 2021

@author: shixiaohan
"""

from typing import List

class Solution:
    '''
    def permute(nums):
        def dfs(nums, size, depth, path, state, res):
            if depth == size:
                res.append(path)
                return

            for i in range(size):
                if ((state >> i) & 1) == 0:
                    dfs(nums, size, depth + 1, path + [nums[i]], state ^ (1 << i), res)

        size = len(nums)
        if size == 0:
            return []

        state = 0
        res = []
        dfs(nums, size, 0, [], state, res)
        return res
    '''
    def permute(nums):
        res = []
        path = []
        def backtrack(nums):
            if(len(path) == len(nums)):
                res.append(path[:])
                return
            for i in range(0,len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop()
        backtrack(nums)
        return res
        
nums = [1,2,3]
print(Solution.permute(nums))