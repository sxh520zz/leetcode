#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:05:12 2021

@author: shixiaohan
"""


class Solution:
    def splitListToParts(head, k):
        def get_length(root):
            res = 0
            while root:
                res += 1
                root = root.next
            return res
        list_length = get_length(root)
        avg = list_length // k
        m = list_length % k
        ## 每段含有avg个元素，前m段每段多一个元素
        node = root
        res = []
        for i in range(m):   # 前m段
            # avg + 1
            res.append(node)
            for j in range(avg):
                node = node.next
            ## 断开节点
            node.next, node = None, node.next

        for i in range(k-m):  ##  后k-m段
            # avg
            if avg == 0:  ###  装入[]
                res.append(None)
            else:
                res.append(node)
                for j in range(avg-1):
                    node = node.next
                ## 断开节点
                node.next, node = None, node.next
        return res

head = [1,2,3]
k = 5
print(Solution.splitListToParts(head, k))
