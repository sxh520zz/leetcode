#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:12:14 2021

@author: shixiaohan
"""


class Solution(object):
    def maxAreaOfIsland(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        :type prices: List[int]
        :rtype: int
        """
        def dfs(r: int, c: int) -> None:
            nonlocal res
            
            grid[r][c] = -1
            cnt = 1
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < Row and 0 <= nc < Col and grid[nr][nc] == 1:
                    cnt += dfs(nr, nc)
            res = max(res, cnt)
            return cnt

        Row = len(grid)
        Col = len(grid[0])
       
        res = 0
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1:
                    dfs(r, c)
        return res
        
      
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution.maxAreaOfIsland(grid))