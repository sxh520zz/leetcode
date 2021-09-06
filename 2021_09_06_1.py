#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:09:40 2021

@author: shixiaohan
"""


class Solution:
    def search(nums, target):
        head = 0
        tail = len(nums)-1
        while(head <= tail):
            mid = (head + tail) // 2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                head = mid +1
            elif(nums[mid] > target):
                tail = mid -1
        return -1

nums = [2,5]
target = 3

print(Solution.search(nums,target))