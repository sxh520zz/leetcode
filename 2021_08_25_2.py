#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:19:59 2021

@author: shixiaohan
"""

class Solution(object):
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans
                
prices = [5,7,1,8]

print(Solution.maxProfit(prices))