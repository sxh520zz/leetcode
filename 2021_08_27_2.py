#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:30:54 2021

@author: shixiaohan
"""


class Solution(object):
    def singleNonDuplicate(nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1   
        while lo < hi:
            mid = lo + (hi - lo) // 2
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]
        
      
nums = [1,1,2]
print(Solution.singleNonDuplicate(nums))