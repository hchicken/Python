#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 08:31
# @Author  : Greens


"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""


def main(n):
    dp = [0] * (n + 1)  # 定义一个长度为n+1的数组
    # 长度0 和 1 的绳子无法切
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], max(dp[i - j] * j, j * (i - j)))

    print(dp)


if __name__ == '__main__':
    main(18)
