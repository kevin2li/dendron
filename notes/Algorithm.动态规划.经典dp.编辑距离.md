---
id: gbbtxdg4glp15jfqevj66k1
title: 编辑距离
desc: ''
updated: 1682752345406
created: 1682752286915
---

参考: https://the-algorithms.com/algorithm/edit-distance

``` python 
"""
Author  : Turfa Auliarachman
Date    : October 12, 2016

This is a pure Python implementation of Dynamic Programming solution to the edit
distance problem.

The problem is :
Given two strings A and B. Find the minimum number of operations to string B such that
A = B. The permitted operations are removal,  insertion, and substitution.
"""

def min_dist_bottom_up(self, word1: str, word2: str) -> int:
    """
    >>> EditDistance().min_dist_bottom_up("intention", "execution")
    5
    >>> EditDistance().min_dist_bottom_up("intention", "")
    9
    >>> EditDistance().min_dist_bottom_up("", "")
    0
    """
    self.word1 = word1
    self.word2 = word2
    m = len(word1)
    n = len(word2)
    self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:  # first string is empty
                self.dp[i][j] = j
            elif j == 0:  # second string is empty
                self.dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:  # last characters are equal
                self.dp[i][j] = self.dp[i - 1][j - 1]
            else:
                insert = self.dp[i][j - 1]
                delete = self.dp[i - 1][j]
                replace = self.dp[i - 1][j - 1]
                self.dp[i][j] = 1 + min(insert, delete, replace)
    return self.dp[m][n]
```