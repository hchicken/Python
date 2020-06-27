#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 18:02
# @Author  : Greens


"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18
"""


class Solution:
    def cutRope(self, number):
        dp = [0 for _ in range(number + 1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, number + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        print(dp)
        return dp[number]


if __name__ == '__main__':
    my_class = Solution()
    my_class.cutRope(9)
