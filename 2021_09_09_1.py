#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 23:27:54 2021

@author: shixiaohan
"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

nums = [-1,0,1,2,-1,-4]
print(Solution.hasCycle(nums))