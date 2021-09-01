#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:04:18 2021

@author: shixiaohan
"""


class Solution(object):
    def rob(nums):
        """
        :type n: int
        :rtype: int
        """
        '''
        if(len(nums) ==1):
            return nums[0]
        if(len(nums) ==2):
            return max(len(0),len(1))
        
        dp = [max(len(0),len(1))]
        for i in range(2,len(nums)-1):
        '''
        if len(nums) == 0:
            return 0
    
        # 子问题：
        # f(k) = 偷 [0..k) 房间中的最大金额
    
        # f(0) = 0
        # f(1) = nums[0]
        # f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }
    
        N = len(nums)
        dp = [0] * (N+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N+1):
            dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])
        return dp[N]


nums=[2,7,9,3,1]
print(Solution.rob(nums))