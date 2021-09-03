#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:15:04 2021

@author: shixiaohan
"""


class Solution(object):
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = 0
        num_2 = 0
        for i in range(len(l1)-1,-1,-1):
            num_1 += 10**i * l1[i]
        for i in range(len(l2)-1,-1,-1):
            num_2 += 10**i * l2[i] 
        
        num_out = num_1 + num_2
        
        if(num_out == 0):
            return num_out
        else:
            a = []
            while num_out != 0:
                a.append(num_out%10)
                num_out = int(num_out/10)
            return a

l1 = [2,4,3]

l2 = [5,6,4]
print(Solution.addTwoNumbers(l1, l2))