#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:56:13 2021

@author: shixiaohan
"""


import math

class Solution(object):
    def judgeSquareSum(c):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        a = 0
        b = int(math.sqrt(c))
       
        while(a <= b):
            if((a*a + b*b) <c):
                a = a+1
            elif((a*a + b*b) >c):
                b = b-1
            elif((a*a + b*b) ==c):
                return True
        return False

c = 5
print(Solution.judgeSquareSum(c))