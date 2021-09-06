#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:59:11 2021

@author: shixiaohan
"""



class Solution:
    def dailyTemperatures(temperatures):
        '''
        max_tem = 0
        out_list = [0*len(temperatures)-1]
        for i in range(len(temperatures)-1):
            max_tem = temperatures[i]
            if(max_tem < temperatures[i+1]):
                out_list[i] = 1
                max_tem = out_list[i]
            else:
                out_list[i] = 0
        '''
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n):
            if i == 0:
                stack.append((temperatures[i], 0))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    item = stack.pop()
                    ans[item[1]] = i - item[1]
                stack.append((temperatures[i],i))
        return ans

temperatures = [73,74,75,71,69,72,76,73]
print(Solution.dailyTemperatures(temperatures))