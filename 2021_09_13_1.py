#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:23:23 2021

@author: shixiaohan
"""

class Solution:
    def maxProfit(prices):
        '''
        num = []
        for i in range(len(prices)):
            x = 0
            for j in range(len(prices)):
                if(i >= j):
                    max_data = prices[i]-prices[j]
                    if(x < max_data):
                        x=max_data
            num.append(x)
        return max(num)
        '''
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

                           
prices = [7,6,4,3,1]
print(Solution.maxProfit(prices))
