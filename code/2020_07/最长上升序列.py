#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 07:07
# @Author  : Greens


"""
最长上升子序列（LIS）问题：给定长度为n的序列a，从a中抽取出一个子序列，这个子序列需要单调递增。
问最长的上升子序列（LIS）的长度。
e.g:1,5,3,4,6,9,7,8 的LIS为1,3,4,6,7,8，长度为6
"""


def lis(nums):
    if not nums:
        return 0

    dp = []
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)


if __name__ == '__main__':
    my_list = [1, 5, 3, 4, 6, 9, 7, 8]
    lis(my_list)
