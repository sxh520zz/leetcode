#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:53:10 2021

@author: shixiaohan
"""


class Solution:
    def eraseOverlapIntervals(intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        
        return n - ans

intervals = [[1,2],[2,3],[3,4],[1,3]]

print(Solution.eraseOverlapIntervals(intervals))