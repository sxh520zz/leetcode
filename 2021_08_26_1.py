#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:16:25 2021

@author: shixiaohan
"""

class Solution(object):
    def mySqrt(x):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        while i *i <= x:
            i = i+1
        return i-1
                
x = 4

print(Solution.mySqrt(x))