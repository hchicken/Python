#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 22:27
# @Author  : Greens

"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

"""
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        # 求出开方值
        num = int(math.exp(0.5 * math.log(x)))
        return num + 1 if (num + 1) ** 2 <= x else num


# class Solution:
#     # 二分法
#     def mySqrt(self, x: int) -> int:
#         l, r, ret = 0, x, 0
#         while l <= r:
#             mid = (l + r) // 2
#             if mid * mid <= x:
#                 ret = mid
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return ret


if __name__ == "__main__":
    my_int = 2147395600
    my_class = Solution()
    my_def = my_class.mySqrt(my_int)
    print(my_def)
