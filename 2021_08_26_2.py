#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:29:01 2021

@author: shixiaohan
"""

class Solution(object):
     def searchRange(nums, target):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(nums)
        index_right = -1
        index_left = -1
        error = [-1,-1]
        out = []
        if(len(nums) != 0):
            for i in range(len(nums)):
                if(nums[i] == target):
                    index_right = i
                    break
            for i in range(length-1,-1,-1):
                if(nums[i] == target):
                    index_left = i
                    break
            if(index_right==-1 and index_right==-1):
                return error
            else:
                out.append(index_right)
                out.append(index_left)
                return out
        else:
            return error
        
nums = [2,5,6,0,0,1,2]
target = 0
print(Solution.searchRange(nums,target))