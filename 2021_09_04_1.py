#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 23:35:24 2021

@author: shixiaohan
"""


class Solution(object):
    def singleNumber(nums):
        nums = sorted(nums)
        print(nums)
        leng = len(nums)
        for i in range(1,leng-1,1):
            if(nums[i] != nums[i-1] and i %2 ==1):
                return nums[i-1]
        return nums[-1]

nums = [4,1,2,1,2]
print(Solution.singleNumber(nums))