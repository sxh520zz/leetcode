#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:55:51 2021

@author: shixiaohan
"""


class Solution(object):
    def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,2]
        
        for i in range(2,n):
            dp_instert = dp[i-1]+dp[i-2]
            dp.append(dp_instert)
        return dp[-1]
n=5
print(Solution.climbStairs(n))