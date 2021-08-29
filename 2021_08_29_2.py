#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:18:10 2021

@author: shixiaohan
"""

class Solution(object):
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if(m != 0 and n != 0):
            for i in range(m,len(nums1),1):
                nums1[i] = nums2[i-3] 
            nums1.sort()
            return nums1
        elif(m == 0): return nums2
        elif(n == 0): return nums1

[0]
0
[1]
1

nums1 = [0]
m = 0
nums2 = [1]
n = 1

print(Solution.merge(nums1, m, nums2, n))