#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:15:05 2021

@author: shixiaohan
"""


class Solution(object):
     def findMin(nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: left = mid + 1
            elif nums[mid] < nums[right]: right = mid
            else: right = right - 1 # key
        return nums[left]       
        
nums = [1,3,5]
print(Solution.findMin(nums))