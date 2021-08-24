#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:01:04 2021

@author: shixiaohan
"""

import copy

class Solution(object):
    def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed_print = copy.copy(flowerbed)
        num = 0
        if(len(flowerbed) == 1 and flowerbed[0] == 0):
            num += 1
        for i in range(len(flowerbed)-1):
            if(i == 0):
                if(flowerbed[i+1] != 1):
                    flowerbed[i] = 1   
            if(i > 0):
                if(flowerbed[i-1] != 1 and flowerbed[i+1] != 1):
                    flowerbed[i] = 1
            if(i+1 == len(flowerbed)-1):
                if(flowerbed[i+1] != 1 and flowerbed[i] != 1):
                    flowerbed[-1] = 1
        for i in range(len(flowerbed)):
            if(flowerbed[i] != flowerbed_print[i]):
                num += 1
        if(num >= n):
            return True
        else:
            return False
flowerbed = [0]
n = 1

print(Solution.canPlaceFlowers(flowerbed,n))