#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:40:48 2021

@author: shixiaohan
"""


class Solution:
    def lengthOfLongestSubstring(s):
        '''
        if(len(s) == 1 or len(s) == 0):
            return len(s)
        out = []
        a = []
        for i in s:
            if i not in a:
                a.append(i)
            else:
                out.append(len(a))
                a= a[-1:]
                if(i == a[-1:][0]):
                    continue
                else:
                    a.append(i) 
                
        out.append(len(a))   
        if(len(out) != 0):
            return(max(out))
        else:
            return(len(a))
        '''
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        
        return len(lookup)
        
s = "anviaj"
print(Solution.lengthOfLongestSubstring(s))