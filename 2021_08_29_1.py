#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:33:53 2021

@author: shixiaohan
"""


class Solution(object):
    def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)- 1
        while (l < r):
            num_sum = numbers[l] + numbers[r];
            if (num_sum == target):
                break
            if (num_sum < target):
                l = l+1
            else:
                r= r-1
        out = [l+1,r+1]
        return out



numbers = [-4,2,3]
target = -2
print(Solution.twoSum(numbers,target))