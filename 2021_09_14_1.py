#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:11:48 2021

@author: shixiaohan
"""

class Solution:
    def findLongestWord(s, dictionary):
        '''
        length_dic = []
        for i in range(len(dictionary)):
            length_dic.append(len(dictionary[i]))
        while len(length_dic) != 0:
            dix = length_dic.index(max(length_dic))
            flag = True
            for i in range(len(dictionary[dix])):
                if dictionary[dix][i] in s:
                    continue
                else:
                    flag = -1
            if(flag == True):
                return dictionary[dix]
            del length_dic[dix]
            del dictionary[dix]     
        '''
        dictionary.sort(key=lambda x: (-len(x), x))
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                return t
        return ""
          
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]

print(Solution.findLongestWord(s,dictionary))
