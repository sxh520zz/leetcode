#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:28:39 2021

@author: shixiaohan
"""


class Solution:
    def balancedStringSplit(s):
        ans, d = 0, 0
        for ch in s:
            if ch == 'L':
                d += 1
            else:
                d -= 1
            if d == 0:
                ans += 1
        return ans


        
s = "RLRRLLRLRL"
print(Solution.balancedStringSplit(s))