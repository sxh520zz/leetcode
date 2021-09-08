#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:36:05 2021

@author: shixiaohan
"""

class Solution:
    def threeSum(nums):
        n = len(nums)
        res = []
        if(not nums or n<3):
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if(nums[i] > 0):
                return res
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res

                    
        
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))