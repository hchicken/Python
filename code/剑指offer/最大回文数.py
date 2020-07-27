#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 07:22
# @Author  : Greens


def find(nums):
    """
    查询回文数
    """
    n = len(nums)  # 字符串长度

    max_str = ""

    dp = [[False] * n for _ in range(n)]
    # 开始——结束 index 的差值
    for l in range(n):

        for start in range(n):
            end = start + l

            # index 超过
            if end >= n:
                break

            # 一个字符，本来就是回文数
            if l == 0:
                dp[start][end] = True

            # 2个字符，判断2个字符是否相等
            elif l == 1:
                dp[start][end] = nums[start] == nums[end]

            # 大于2个字符，判断 l-1个字符是不是回文 且 start == end
            else:
                dp[start][end] = dp[start + 1][end - 1] and nums[start] == nums[end]

            if dp[start][end] and l + 1 > len(max_str):
                max_str = nums[start: end + 1]
    print(max_str)


if __name__ == '__main__':
    s = "1212134"
    find(s)
