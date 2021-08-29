#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:56:13 2021

@author: shixiaohan
"""

def check(s, lo, hi):
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True
class Solution(object):

    def validPalindrome(s):
        """
        :type head: ListNode
        :rtype: ListNode
        """
   
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            if s[l] != s[r]:
                return check(s, l + 1, r) or check(s, l, r - 1)
            l += 1
            r -= 1
        return True


        
        

s = 'abca'
print(Solution.validPalindrome(s))