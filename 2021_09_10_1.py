#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 23:06:32 2021

@author: shixiaohan
"""
        
class Solution:
    def chalkReplacer(chalk,k):
        sum_one_turn = sum(chalk)
        turn = k%sum_one_turn
        cha = 0
        for i in range(len(chalk)):
            cha += chalk[i]
            if(cha > turn):
                return i
            

                    
        
chalk = [3,4,1,2]
k = 2
print(Solution.chalkReplacer(chalk,k))

