#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:46:20 2021

@author: shixiaohan
"""


class Solution(object):
     def search(nums, target):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(nums) == 1 and target == 1):
            return True
        elif(len(nums) == 1 and target == 0):
            return False    
        else:
            if(target>0):
                out_data = nums[target:]
                out_data.extend(nums[:target])
            else:
                out_data = nums
            if target in out_data:
                return True
            else:
                return False
                    
            
        
nums = [1,1]
target = 1
print(Solution.search(nums,target))