# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2020/1/8 22:04


"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。
"""


class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     n1 = int(a, 2)
    #     n2 = int(b, 2)
    #     n = n1 + n2
    #     return str(bin(n))[2:]

    def addBinary(self, a: str, b: str) -> str:
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return '1' + r if p else r


if __name__ == "__main__":
    my_class = Solution()
    a = "10111"
    b = "111"
    my_def = my_class.addBinary(a, b)
    print(my_def)
