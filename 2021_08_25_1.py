#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:20:21 2021

@author: shixiaohan
"""

import copy

class Solution(object):
    def checkPossibility(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index=-1;
        #统计nums[i]>nums[i+1]的出现次数
        cnt=0;
        for i in range (len(nums)-1):
            if(nums[i]<=nums[i+1]):
                continue;
            cnt = cnt+1
            index=i
        #nums[i]>nums[i+1]出现的次数不仅一次
        if(cnt>1):
            return False;
        #处理边界情况     
        if(index==-1 or index==0 or index==len(nums)-2):
            return True;
        #分为两种情况，并进行判断
        after=nums[index+2];
        ibefore=nums[index-1];
        if(after>=nums[index] or before<=nums[index+1]):
            return True;
        return False;
                
            
                
nums = [5,7,1,8]

print(Solution.checkPossibility(nums))